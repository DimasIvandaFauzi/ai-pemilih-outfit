from flask import Flask, render_template, request, jsonify
from fuzzywuzzy import fuzz
from outfit_data import outfit_rekomendasi, event_list

app = Flask(__name__)

def calculate_confidence(selected_items, checklist, aturan):
    # Hitung total bobot item yang dipilih
    total_bobot = 0
    item_confidences = {}
    selected_categories = set()
    
    # Kumpulkan bobot dan kategori item yang dipilih
    for item in selected_items:
        for category, items in checklist.items():
            for cat_item in items:
                if cat_item['item'] == item:
                    total_bobot += cat_item['bobot']
                    selected_categories.add(category)
                    # Hitung confidence per item (bobot relatif terhadap max bobot kategori)
                    max_bobot_cat = max(i['bobot'] for i in items)
                    item_confidence = (cat_item['bobot'] / max_bobot_cat) * 100
                    item_confidences[item] = round(item_confidence, 2)
    
    # Hitung total bobot maksimum dari semua item di checklist
    max_bobot = sum(item['bobot'] for cat in checklist.values() for item in cat)
    
    # Hitung confidence keseluruhan
    overall_confidence = (total_bobot / max_bobot) * 100 if max_bobot > 0 else 0
    overall_confidence = round(min(overall_confidence, 100), 2)
    
    # Evaluasi aturan rekomendasi
    recommendations = []
    tips = []
    for rule in aturan:
        matched_items = [item for item in selected_items if item in rule['kombinasi']]
        rule_bobot = sum(
            next(i['bobot'] for i in checklist[cat] if i['item'] == item)
            for cat in checklist for item in matched_items if item in [it['item'] for it in checklist[cat]]
        )
        
        if rule_bobot >= rule['bobot_min']:
            confidence = min(rule['confidence_base'], overall_confidence + 10)
            recommendations.append({
                'nama': rule['nama'],
                'confidence': round(confidence, 2),
                'deskripsi': rule['deskripsi'],
                'outfit_items': matched_items
            })
        else:
            # Tambahkan tips untuk item yang kurang dari aturan
            missing_items = [item for item in rule['kombinasi'] if item not in selected_items]
            for missing_item in missing_items:
                tips.append(f"Pilih {missing_item} untuk meningkatkan tampilan sesuai gaya {rule['nama']}.")
    
    # Tambahkan tips umum jika bobot rendah
    if total_bobot < 0.5 * max_bobot:
        for category, items in checklist.items():
            high_bobot_items = sorted(items, key=lambda x: x['bobot'], reverse=True)[:2]
            for item in high_bobot_items:
                if item['item'] not in selected_items:
                    tips.append(f"Pertimbangkan {item['item']} untuk kesan lebih rapi dan sesuai acara.")
    
    return overall_confidence, item_confidences, recommendations, tips

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/templates/match-outfit-to-event.html')
def match_outfit():
    return render_template('match-outfit-to-event.html', event_list=event_list)

@app.route('/templates/pilih_gender.html')
def pilih_gender():
    event = request.args.get('event', '').lower()
    if not event or event not in outfit_rekomendasi:
        return render_template('pilih_gender.html', event="Tidak ditemukan", valid_event=False)
    return render_template('pilih_gender.html', event=event, valid_event=True)

@app.route('/templates/checklist.html')
def checklist():
    event = request.args.get('event', '').lower()
    gender = request.args.get('gender', '').lower()
    if not event or event not in outfit_rekomendasi or gender not in ['pria', 'wanita']:
        return render_template('checklist.html', event="Tidak ditemukan", checklist=None, gender=gender)
    return render_template('checklist.html', event=event, checklist=outfit_rekomendasi[event]['checklist'][gender], gender=gender)

@app.route('/templates/final.html', methods=['GET', 'POST'])
def final():
    if request.method == 'POST':
        event = request.form.get('event', '').lower()
        gender = request.form.get('gender', '').lower()
        selected_items = request.form.getlist('items')
        
        if not event or event not in outfit_rekomendasi or gender not in ['pria', 'wanita']:
            return render_template('final.html', 
                                 event=None,
                                 error="Maaf, acara atau gender tidak valid.",
                                 gender=gender,
                                 recommendations=[],
                                 selected_items=[],
                                 item_confidences={},
                                 overall_confidence=0,
                                 tips=[])
        
        checklist = outfit_rekomendasi[event]['checklist'][gender]
        aturan = outfit_rekomendasi[event]['aturan'][gender]
        
        # Validasi minimal satu item per kategori
        selected_categories = set()
        for item in selected_items:
            for category, items in checklist.items():
                if any(check_item['item'] == item for check_item in items):
                    selected_categories.add(category)
        
        if len(selected_categories) < len(checklist):
            return render_template('checklist.html', 
                                 event=event, 
                                 checklist=checklist, 
                                 gender=gender,
                                 error="Pilih minimal satu item dari setiap kategori (atasan, bawahan, aksesori).")
        
        # Hitung kecocokan dan rekomendasi
        overall_confidence, item_confidences, recommendations, tips = calculate_confidence(selected_items, checklist, aturan)
        
        return render_template('final.html', 
                             event=event.capitalize(),
                             recommendations=recommendations,
                             selected_items=selected_items,
                             item_confidences=item_confidences,
                             overall_confidence=overall_confidence,
                             tips=tips,
                             gender=gender,
                             error=None)
    
    return render_template('final.html', 
                         event=None,
                         recommendations=[],
                         selected_items=[],
                         item_confidences={},
                         overall_confidence=0,
                         tips=[],
                         gender=None,
                         error="Silakan pilih event dan gender terlebih dahulu.")

@app.route('/search', methods=['POST'])
def search_event():
    event_input = request.form.get('event_input', '').lower().strip()
    if not event_input:
        return jsonify({'error': 'Masukkan nama acara.'})

    best_match = None
    highest_score = 0
    for event in event_list:
        score = fuzz.partial_ratio(event_input, event)
        if score > highest_score and score > 70:
            highest_score = score
            best_match = event

    if best_match:
        data = outfit_rekomendasi.get(best_match, {})
        return jsonify({
            'event': best_match.capitalize(),
            'deskripsi': data.get('deskripsi', {}),
            'gender': data.get('kategori', ''),
            'checklist': data.get('checklist', {})
        })
    return jsonify({'error': 'Acara tidak ditemukan.'})

if __name__ == '__main__':
    app.run(debug=True)