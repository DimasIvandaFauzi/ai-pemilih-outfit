from flask import Flask, render_template, request, jsonify
from fuzzywuzzy import fuzz
import uuid

app = Flask(__name__)

# Data rekomendasi outfit dengan checklist spesifik gender
outfit_rekomendasi = {
    "kuliah": {
        "deskripsi": {
            "pria": "Kaos polo atau kemeja flanel kasual, celana chino atau jeans slim-fit, sepatu sneakers atau loafers, ransel praktis.",
            "wanita": "Atasan blouse kasual atau kaos nyaman, celana jeans skinny atau kulot, sepatu sneakers atau flat shoes, tote bag atau ransel."
        },
        "aksesori": {
            "pria": ["Ransel", "Jam tangan", "Topi baseball"],
            "wanita": ["Tote bag", "Syal ringan", "Kacamata baca"]
        },
        "kategori": "kasual",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kaos polo", "bobot": 0.35},
                    {"item": "Kemeja flanel", "bobot": 0.3},
                    {"item": "Kaos nyaman", "bobot": 0.25},
                    {"item": "Kemeja lengan pendek", "bobot": 0.2},
                    {"item": "Hoodie kasual", "bobot": 0.2},
                    {"item": "Sweater crew neck", "bobot": 0.15}
                ],
                "bawahan": [
                    {"item": "Celana chino", "bobot": 0.35},
                    {"item": "Celana jeans slim-fit", "bobot": 0.3},
                    {"item": "Celana jogger", "bobot": 0.25},
                    {"item": "Celana pendek kasual", "bobot": 0.2}
                ],
                "aksesori": [
                    {"item": "Ransel", "bobot": 0.3},
                    {"item": "Jam tangan", "bobot": 0.2},
                    {"item": "Topi baseball", "bobot": 0.15},
                    {"item": "Kacamata hitam", "bobot": 0.1}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Blouse kasual", "bobot": 0.35},
                    {"item": "Kaos nyaman", "bobot": 0.3},
                    {"item": "Kemeja lengan pendek", "bobot": 0.25},
                    {"item": "Cardigan tipis", "bobot": 0.2},
                    {"item": "Sweater longgar", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana jeans skinny", "bobot": 0.35},
                    {"item": "Celana kulot", "bobot": 0.3},
                    {"item": "Celana palazzo", "bobot": 0.25},
                    {"item": "Rok denim", "bobot": 0.2},
                    {"item": "Legging kasual", "bobot": 0.15}
                ],
                "aksesori": [
                    {"item": "Tote bag", "bobot": 0.3},
                    {"item": "Syal ringan", "bobot": 0.2},
                    {"item": "Kacamata baca", "bobot": 0.15},
                    {"item": "Gelang simpel", "bobot": 0.1}
                ]
            }
        }
    },
    "nikahan": {
        "deskripsi": {
            "pria": "Setelan jas slim-fit warna gelap, kemeja putih, dasi sutra, sepatu kulit formal, atau batik modern dengan celana bahan.",
            "wanita": "Gaun midi elegan dengan detail renda, kebaya modern dengan kain songket, sepatu hak tinggi, clutch kecil."
        },
        "aksesori": {
            "pria": ["Dasi sutra", "Jam tangan elegan", "Ikat pinggang kulit"],
            "wanita": ["Clutch elegan", "Sepatu hak tinggi", "Anting minimalis"]
        },
        "kategori": "formal",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Jas slim-fit", "bobot": 0.4},
                    {"item": "Kemeja putih", "bobot": 0.35},
                    {"item": "Batik modern", "bobot": 0.3},
                    {"item": "Kemeja formal", "bobot": 0.25},
                    {"item": "Vest formal", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana bahan", "bobot": 0.4},
                    {"item": "Celana formal", "bobot": 0.35},
                    {"item": "Celana tailored", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Dasi sutra", "bobot": 0.3},
                    {"item": "Jam tangan elegan", "bobot": 0.25},
                    {"item": "Ikat pinggang kulit", "bobot": 0.2},
                    {"item": "Sepatu kulit", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Gaun midi", "bobot": 0.4},
                    {"item": "Kebaya modern", "bobot": 0.35},
                    {"item": "Blouse elegan", "bobot": 0.3},
                    {"item": "Atasan renda", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Rok songket", "bobot": 0.4},
                    {"item": "Rok midi", "bobot": 0.35},
                    {"item": "Celana bahan", "bobot": 0.3},
                    {"item": "Rok A-line", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Clutch elegan", "bobot": 0.3},
                    {"item": "Sepatu hak tinggi", "bobot": 0.25},
                    {"item": "Anting minimalis", "bobot": 0.2},
                    {"item": "Kalung simpel", "bobot": 0.15}
                ]
            }
        }
    },
    "pantai": {
        "deskripsi": {
            "pria": "Kaos tipis berbahan linen, celana pendek chino, sandal jepit kulit, topi jerami untuk perlindungan matahari.",
            "wanita": "Maxi dress berbahan katun dengan motif floral, sandal jepit, topi pantai lebar, kacamata hitam."
        },
        "aksesori": {
            "pria": ["Topi jerami", "Kacamata hitam", "Sandal jepit"],
            "wanita": ["Topi pantai lebar", "Kacamata hitam", "Tote bag kanvas"]
        },
        "kategori": "kasual",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kaos linen", "bobot": 0.35},
                    {"item": "Kemeja pantai", "bobot": 0.3},
                    {"item": "Kaos tipis", "bobot": 0.25},
                    {"item": "Tank top kasual", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana pendek chino", "bobot": 0.35},
                    {"item": "Celana pendek denim", "bobot": 0.3},
                    {"item": "Celana pendek kasual", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Topi jerami", "bobot": 0.3},
                    {"item": "Kacamata hitam", "bobot": 0.25},
                    {"item": "Sandal jepit", "bobot": 0.2},
                    {"item": "Tote bag kanvas", "bobot": 0.15}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Maxi dress", "bobot": 0.4},
                    {"item": "Kaos tipis", "bobot": 0.3},
                    {"item": "Blouse pantai", "bobot": 0.25},
                    {"item": "Tank top kasual", "bobot": 0.2},
                    {"item": "Kemeja oversized", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Rok maxi", "bobot": 0.35},
                    {"item": "Celana pendek kasual", "bobot": 0.3},
                    {"item": "Celana palazzo", "bobot": 0.25},
                    {"item": "Rok pendek", "bobot": 0.2}
                ],
                "aksesori": [
                    {"item": "Topi pantai lebar", "bobot": 0.3},
                    {"item": "Kacamata hitam", "bobot": 0.25},
                    {"item": "Tote bag kanvas", "bobot": 0.2},
                    {"item": "Sandal jepit", "bobot": 0.2}
                ]
            }
        }
    },
    "kantor": {
        "deskripsi": {
            "pria": "Kemeja oxford lengan panjang, celana chino tailored, ikat pinggang kulit, sepatu loafer formal.",
            "wanita": "Blazer terstruktur, kemeja sutra, rok pensil selutut, sepatu flat atau hak rendah, tas kerja kulit."
        },
        "aksesori": {
            "pria": ["Jam tangan klasik", "Ikat pinggang kulit", "Kacamata formal"],
            "wanita": ["Tote bag kulit", "Jam tangan klasik", "Kacamata formal"]
        },
        "kategori": "formal",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kemeja oxford", "bobot": 0.4},
                    {"item": "Kemeja formal", "bobot": 0.35},
                    {"item": "Blazer", "bobot": 0.3},
                    {"item": "Kemeja lengan panjang", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Celana chino tailored", "bobot": 0.4},
                    {"item": "Celana bahan", "bobot": 0.35},
                    {"item": "Celana formal", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Ikat pinggang kulit", "bobot": 0.3},
                    {"item": "Jam tangan klasik", "bobot": 0.25},
                    {"item": "Kacamata formal", "bobot": 0.2},
                    {"item": "Sepatu loafer formal", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Blazer terstruktur", "bobot": 0.4},
                    {"item": "Kemeja sutra", "bobot": 0.35},
                    {"item": "Blouse formal", "bobot": 0.3},
                    {"item": "Kemeja lengan panjang", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Rok pensil", "bobot": 0.4},
                    {"item": "Celana bahan tailored", "bobot": 0.35},
                    {"item": "Rok midi", "bobot": 0.3},
                    {"item": "Celana formal", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Tote bag kulit", "bobot": 0.3},
                    {"item": "Jam tangan klasik", "bobot": 0.25},
                    {"item": "Kacamata formal", "bobot": 0.2},
                    {"item": "Sepatu hak rendah", "bobot": 0.25}
                ]
            }
        }
    },
    "olahraga": {
        "deskripsi": {
            "pria": "Kaos olahraga dry-fit dengan ventilasi, celana training pendek elastis, sepatu lari dengan bantalan maksimal.",
            "wanita": "Sports bra berdaya dukung tinggi, tank top teknis, legging olahraga dengan saku, sepatu lari ringan."
        },
        "aksesori": {
            "pria": ["Botol air", "Smartwatch olahraga", "Ikat kepala"],
            "wanita": ["Botol air", "Smartwatch olahraga", "Ikat kepala"]
        },
        "kategori": "olahraga",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kaos dry-fit", "bobot": 0.4},
                    {"item": "Tank top olahraga", "bobot": 0.35},
                    {"item": "Kaos teknis", "bobot": 0.3},
                    {"item": "Hoodie olahraga", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Celana training pendek", "bobot": 0.4},
                    {"item": "Celana jogger olahraga", "bobot": 0.35},
                    {"item": "Celana pendek olahraga", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Botol air", "bobot": 0.3},
                    {"item": "Smartwatch olahraga", "bobot": 0.25},
                    {"item": "Ikat kepala", "bobot": 0.2},
                    {"item": "Sepatu lari", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Sports bra", "bobot": 0.4},
                    {"item": "Tank top teknis", "bobot": 0.35},
                    {"item": "Kaos olahraga", "bobot": 0.3},
                    {"item": "Hoodie olahraga", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Legging olahraga", "bobot": 0.4},
                    {"item": "Celana pendek olahraga", "bobot": 0.35},
                    {"item": "Celana jogger olahraga", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Botol air", "bobot": 0.3},
                    {"item": "Smartwatch olahraga", "bobot": 0.25},
                    {"item": "Ikat kepala", "bobot": 0.2},
                    {"item": "Sepatu lari ringan", "bobot": 0.25}
                ]
            }
        }
    },
    "nongkrong": {
        "deskripsi": {
            "pria": "Kaos santai dengan motif simpel, celana jeans slim-fit, sneakers kasual, topi baseball.",
            "wanita": "Kemeja kasual oversized, celana jeans high-waist, sepatu kets, tas selempang kecil."
        },
        "aksesori": {
            "pria": ["Topi baseball", "Kacamata hitam", "Tas selempang"],
            "wanita": ["Tas selempang", "Kacamata hitam", "Topi baseball"]
        },
        "kategori": "kasual",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kaos santai", "bobot": 0.35},
                    {"item": "Kemeja kasual", "bobot": 0.3},
                    {"item": "Sweater crew neck", "bobot": 0.25},
                    {"item": "Hoodie simpel", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana jeans slim-fit", "bobot": 0.35},
                    {"item": "Celana chino", "bobot": 0.3},
                    {"item": "Celana jogger", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Topi baseball", "bobot": 0.3},
                    {"item": "Kacamata hitam", "bobot": 0.25},
                    {"item": "Tas selempang", "bobot": 0.2},
                    {"item": "Sneakers kasual", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Kemeja oversized", "bobot": 0.35},
                    {"item": "Kaos santai", "bobot": 0.3},
                    {"item": "Sweater tipis", "bobot": 0.25},
                    {"item": "Blouse kasual", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana jeans high-waist", "bobot": 0.35},
                    {"item": "Celana kulot", "bobot": 0.3},
                    {"item": "Rok denim", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Tas selempang", "bobot": 0.3},
                    {"item": "Kacamata hitam", "bobot": 0.25},
                    {"item": "Topi baseball", "bobot": 0.2},
                    {"item": "Sepatu kets", "bobot": 0.25}
                ]
            }
        }
    },
    "wisuda": {
        "deskripsi": {
            "pria": "Setelan jas formal, kemeja putih, dasi, sepatu kulit, mantel wisuda.",
            "wanita": "Gaun formal panjang, sepatu hak tinggi, mantel wisuda, clutch kecil."
        },
        "aksesori": {
            "pria": ["Dasi", "Jam tangan", "Ikat pinggang kulit"],
            "wanita": ["Clutch", "Anting elegan", "Jam tangan"]
        },
        "kategori": "formal",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Jas formal", "bobot": 0.4},
                    {"item": "Kemeja putih", "bobot": 0.35},
                    {"item": "Vest formal", "bobot": 0.3},
                    {"item": "Mantel wisuda", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Celana formal", "bobot": 0.4},
                    {"item": "Celana tailored", "bobot": 0.35},
                    {"item": "Celana bahan", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Dasi", "bobot": 0.3},
                    {"item": "Jam tangan", "bobot": 0.25},
                    {"item": "Ikat pinggang kulit", "bobot": 0.2},
                    {"item": "Sepatu kulit", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Gaun formal panjang", "bobot": 0.4},
                    {"item": "Kebaya modern", "bobot": 0.35},
                    {"item": "Blouse elegan", "bobot": 0.3},
                    {"item": "Mantel wisuda", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Rok panjang", "bobot": 0.4},
                    {"item": "Rok midi", "bobot": 0.35},
                    {"item": "Celana bahan", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Clutch", "bobot": 0.3},
                    {"item": "Anting elegan", "bobot": 0.25},
                    {"item": "Jam tangan", "bobot": 0.2},
                    {"item": "Sepatu hak tinggi", "bobot": 0.25}
                ]
            }
        }
    },
    "kantor": {
        "deskripsi": {
            "pria": "Kemeja oxford lengan panjang, celana chino tailored, ikat pinggang kulit, sepatu loafer formal.",
            "wanita": "Blazer terstruktur, kemeja sutra, rok pensil selutut, sepatu flat atau hak rendah, tas kerja kulit."
        },
        "aksesori": {
            "pria": ["Jam tangan klasik", "Ikat pinggang kulit", "Kacamata formal"],
            "wanita": ["Tote bag kulit", "Jam tangan klasik", "Kacamata formal"]
        },
        "kategori": "formal",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kemeja oxford", "bobot": 0.4},
                    {"item": "Kemeja formal", "bobot": 0.35},
                    {"item": "Blazer", "bobot": 0.3},
                    {"item": "Kemeja lengan panjang", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Celana chino tailored", "bobot": 0.4},
                    {"item": "Celana bahan", "bobot": 0.35},
                    {"item": "Celana formal", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Ikat pinggang kulit", "bobot": 0.3},
                    {"item": "Jam tangan klasik", "bobot": 0.25},
                    {"item": "Kacamata formal", "bobot": 0.2},
                    {"item": "Sepatu loafer formal", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Blazer terstruktur", "bobot": 0.4},
                    {"item": "Kemeja sutra", "bobot": 0.35},
                    {"item": "Blouse formal", "bobot": 0.3},
                    {"item": "Kemeja lengan panjang", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Rok pensil", "bobot": 0.4},
                    {"item": "Celana bahan tailored", "bobot": 0.35},
                    {"item": "Rok midi", "bobot": 0.3},
                    {"item": "Celana formal", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Tote bag kulit", "bobot": 0.3},
                    {"item": "Jam tangan klasik", "bobot": 0.25},
                    {"item": "Kacamata formal", "bobot": 0.2},
                    {"item": "Sepatu hak rendah", "bobot": 0.25}
                ]
            }
        }
    },
    "olahraga": {
        "deskripsi": {
            "pria": "Kaos olahraga dry-fit dengan ventilasi, celana training pendek elastis, sepatu lari dengan bantalan maksimal.",
            "wanita": "Sports bra berdaya dukung tinggi, tank top teknis, legging olahraga dengan saku, sepatu lari ringan."
        },
        "aksesori": {
            "pria": ["Botol air", "Smartwatch olahraga", "Ikat kepala"],
            "wanita": ["Botol air", "Smartwatch olahraga", "Ikat kepala"]
        },
        "kategori": "olahraga",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kaos dry-fit", "bobot": 0.4},
                    {"item": "Tank top olahraga", "bobot": 0.35},
                    {"item": "Kaos teknis", "bobot": 0.3},
                    {"item": "Hoodie olahraga", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Celana training pendek", "bobot": 0.4},
                    {"item": "Celana jogger olahraga", "bobot": 0.35},
                    {"item": "Celana pendek olahraga", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Botol air", "bobot": 0.3},
                    {"item": "Smartwatch olahraga", "bobot": 0.25},
                    {"item": "Ikat kepala", "bobot": 0.2},
                    {"item": "Sepatu lari", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Sports bra", "bobot": 0.4},
                    {"item": "Tank top teknis", "bobot": 0.35},
                    {"item": "Kaos olahraga", "bobot": 0.3},
                    {"item": "Hoodie olahraga", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Legging olahraga", "bobot": 0.4},
                    {"item": "Celana pendek olahraga", "bobot": 0.35},
                    {"item": "Celana jogger olahraga", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Botol air", "bobot": 0.3},
                    {"item": "Smartwatch olahraga", "bobot": 0.25},
                    {"item": "Ikat kepala", "bobot": 0.2},
                    {"item": "Sepatu lari ringan", "bobot": 0.25}
                ]
            }
        }
    },
    "nongkrong": {
        "deskripsi": {
            "pria": "Kaos santai dengan motif simpel, celana jeans slim-fit, sneakers kasual, topi baseball.",
            "wanita": "Kemeja kasual oversized, celana jeans high-waist, sepatu kets, tas selempang kecil."
        },
        "aksesori": {
            "pria": ["Topi baseball", "Kacamata hitam", "Tas selempang"],
            "wanita": ["Tas selempang", "Kacamata hitam", "Topi baseball"]
        },
        "kategori": "kasual",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kaos santai", "bobot": 0.35},
                    {"item": "Kemeja kasual", "bobot": 0.3},
                    {"item": "Sweater crew neck", "bobot": 0.25},
                    {"item": "Hoodie simpel", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana jeans slim-fit", "bobot": 0.35},
                    {"item": "Celana chino", "bobot": 0.3},
                    {"item": "Celana jogger", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Topi baseball", "bobot": 0.3},
                    {"item": "Kacamata hitam", "bobot": 0.25},
                    {"item": "Tas selempang", "bobot": 0.2},
                    {"item": "Sneakers kasual", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Kemeja oversized", "bobot": 0.35},
                    {"item": "Kaos santai", "bobot": 0.3},
                    {"item": "Sweater tipis", "bobot": 0.25},
                    {"item": "Blouse kasual", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana jeans high-waist", "bobot": 0.35},
                    {"item": "Celana kulot", "bobot": 0.3},
                    {"item": "Rok denim", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Tas selempang", "bobot": 0.3},
                    {"item": "Kacamata hitam", "bobot": 0.25},
                    {"item": "Topi baseball", "bobot": 0.2},
                    {"item": "Sepatu kets", "bobot": 0.25}
                ]
            }
        }
    },
    "kampus": {
        "deskripsi": {
            "pria": "Kaos polo dengan kerah rapi, celana chino, sepatu kets, ransel kasual.",
            "wanita": "Kemeja kasual dengan lengan digulung, celana jeans skinny, sepatu sneakers, tote bag."
        },
        "aksesori": {
            "pria": ["Ransel", "Jam tangan", "Kacamata baca"],
            "wanita": ["Tote bag", "Kacamata baca", "Jam tangan"]
        },
        "kategori": "kasual",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kaos polo", "bobot": 0.35},
                    {"item": "Kemeja kasual", "bobot": 0.3},
                    {"item": "Kaos nyaman", "bobot": 0.25},
                    {"item": "Sweater crew neck", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana chino", "bobot": 0.35},
                    {"item": "Celana jeans", "bobot": 0.3},
                    {"item": "Celana jogger", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Ransel", "bobot": 0.3},
                    {"item": "Jam tangan", "bobot": 0.25},
                    {"item": "Kacamata baca", "bobot": 0.2},
                    {"item": "Sepatu kets", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Kemeja kasual", "bobot": 0.35},
                    {"item": "Kaos polos", "bobot": 0.3},
                    {"item": "Blouse santai", "bobot": 0.25},
                    {"item": "Cardigan tipis", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana jeans skinny", "bobot": 0.35},
                    {"item": "Celana kulot", "bobot": 0.3},
                    {"item": "Rok denim", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Tote bag", "bobot": 0.3},
                    {"item": "Kacamata baca", "bobot": 0.25},
                    {"item": "Jam tangan", "bobot": 0.2},
                    {"item": "Sneakers", "bobot": 0.25}
                ]
            }
        }
    },
    "wisuda": {
        "deskripsi": {
            "pria": "Setelan jas formal, kemeja putih, dasi, sepatu kulit, mantel wisuda.",
            "wanita": "Gaun formal panjang, sepatu hak tinggi, mantel wisuda, clutch kecil."
        },
        "aksesori": {
            "pria": ["Dasi", "Jam tangan", "Ikat pinggang kulit"],
            "wanita": ["Clutch", "Anting elegan", "Jam tangan"]
        },
        "kategori": "formal",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Jas formal", "bobot": 0.4},
                    {"item": "Kemeja putih", "bobot": 0.35},
                    {"item": "Vest formal", "bobot": 0.3},
                    {"item": "Mantel wisuda", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Celana formal", "bobot": 0.4},
                    {"item": "Celana tailored", "bobot": 0.35},
                    {"item": "Celana bahan", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Dasi", "bobot": 0.3},
                    {"item": "Jam tangan", "bobot": 0.25},
                    {"item": "Ikat pinggang kulit", "bobot": 0.2},
                    {"item": "Sepatu kulit", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Gaun formal panjang", "bobot": 0.4},
                    {"item": "Kebaya modern", "bobot": 0.35},
                    {"item": "Blouse elegan", "bobot": 0.3},
                    {"item": "Mantel wisuda", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Rok panjang", "bobot": 0.4},
                    {"item": "Rok midi", "bobot": 0.35},
                    {"item": "Celana bahan", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Clutch", "bobot": 0.3},
                    {"item": "Anting elegan", "bobot": 0.25},
                    {"item": "Jam tangan", "bobot": 0.2},
                    {"item": "Sepatu hak tinggi", "bobot": 0.25}
                ]
            }
        }
    },
    "belanja": {
        "deskripsi": {
            "pria": "Hoodie simpel, celana jeans relaxed-fit, sneakers nyaman, topi snapback.",
            "wanita": "Kaos santai dengan cardigan ringan, celana jeans, sepatu kets, tas belanja kanvas."
        },
        "aksesori": {
            "pria": ["Topi snapback", "Tas belanja kanvas", "Kacamata hitam"],
            "wanita": ["Tas belanja kanvas", "Kacamata hitam", "Topi snapback"]
        },
        "kategori": "kasual",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Hoodie simpel", "bobot": 0.35},
                    {"item": "Kaos santai", "bobot": 0.3},
                    {"item": "Sweater crew neck", "bobot": 0.25},
                    {"item": "Kemeja kasual", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana jeans relaxed-fit", "bobot": 0.35},
                    {"item": "Celana jogger", "bobot": 0.3},
                    {"item": "Celana pendek kasual", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Topi snapback", "bobot": 0.3},
                    {"item": "Tas belanja kanvas", "bobot": 0.25},
                    {"item": "Kacamata hitam", "bobot": 0.2},
                    {"item": "Sneakers nyaman", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Kaos santai", "bobot": 0.35},
                    {"item": "Cardigan ringan", "bobot": 0.3},
                    {"item": "Blouse kasual", "bobot": 0.25},
                    {"item": "Sweater tipis", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana jeans", "bobot": 0.35},
                    {"item": "Celana kulot", "bobot": 0.3},
                    {"item": "Rok denim", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Tas belanja kanvas", "bobot": 0.3},
                    {"item": "Kacamata hitam", "bobot": 0.25},
                    {"item": "Topi snapback", "bobot": 0.2},
                    {"item": "Sepatu kets", "bobot": 0.25}
                ]
            }
        }
    },
    "makan malam": {
        "deskripsi": {
            "pria": "Kemeja lengan panjang slim-fit, celana bahan tailored, sepatu loafers, ikat pinggang kulit.",
            "wanita": "Dress semi-formal selutut dengan detail ruffle, sepatu hak rendah, clutch kecil."
        },
        "aksesori": {
            "pria": ["Jam tangan elegan", "Ikat pinggang kulit", "Kacamata formal"],
            "wanita": ["Clutch", "Jam tangan elegan", "Anting kecil"]
        },
        "kategori": "semi-formal",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kemeja slim-fit", "bobot": 0.4},
                    {"item": "Kemeja lengan panjang", "bobot": 0.35},
                    {"item": "Blazer kasual", "bobot": 0.3},
                    {"item": "Kemeja formal", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Celana bahan tailored", "bobot": 0.4},
                    {"item": "Celana chino", "bobot": 0.35},
                    {"item": "Celana formal", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Jam tangan elegan", "bobot": 0.3},
                    {"item": "Ikat pinggang kulit", "bobot": 0.25},
                    {"item": "Kacamata formal", "bobot": 0.2},
                    {"item": "Sepatu loafers", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Dress semi-formal", "bobot": 0.4},
                    {"item": "Blouse elegan", "bobot": 0.35},
                    {"item": "Kemeja sutra", "bobot": 0.3},
                    {"item": "Atasan ruffle", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Rok selutut", "bobot": 0.4},
                    {"item": "Celana bahan", "bobot": 0.35},
                    {"item": "Rok A-line", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Clutch", "bobot": 0.3},
                    {"item": "Jam tangan elegan", "bobot": 0.25},
                    {"item": "Anting kecil", "bobot": 0.2},
                    {"item": "Sepatu hak rendah", "bobot": 0.25}
                ]
            }
        }
    },
    "bioskop": {
        "deskripsi": {
            "pria": "Sweater crew neck, celana jeans, sneakers, jaket denim ringan.",
            "wanita": "Hoodie oversized, celana jeans skinny, sepatu kets, tas selempang."
        },
        "aksesori": {
            "pria": ["Tas selempang", "Syal ringan", "Kacamata hitam"],
            "wanita": ["Tas selempang", "Syal ringan", "Kacamata hitam"]
        },
        "kategori": "kasual",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Sweater crew neck", "bobot": 0.35},
                    {"item": "Kaos santai", "bobot": 0.3},
                    {"item": "Jaket denim", "bobot": 0.25},
                    {"item": "Hoodie simpel", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana jeans", "bobot": 0.35},
                    {"item": "Celana chino", "bobot": 0.3},
                    {"item": "Celana jogger", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Tas selempang", "bobot": 0.3},
                    {"item": "Syal ringan", "bobot": 0.25},
                    {"item": "Kacamata hitam", "bobot": 0.2},
                    {"item": "Sneakers", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Hoodie oversized", "bobot": 0.35},
                    {"item": "Kaos santai", "bobot": 0.3},
                    {"item": "Sweater tipis", "bobot": 0.25},
                    {"item": "Blouse kasual", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana jeans skinny", "bobot": 0.35},
                    {"item": "Celana kulot", "bobot": 0.3},
                    {"item": "Rok denim", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Tas selempang", "bobot": 0.3},
                    {"item": "Syal ringan", "bobot": 0.25},
                    {"item": "Kacamata hitam", "bobot": 0.2},
                    {"item": "Sepatu kets", "bobot": 0.25}
                ]
            }
        }
    },
    "taman": {
        "deskripsi": {
            "pria": "Kaos nyaman dengan bahan katun, celana pendek cargo, sandal outdoor, topi pet.",
            "wanita": "Dress santai berbahan katun, sepatu kets, topi jerami, tas anyaman."
        },
        "aksesori": {
            "pria": ["Topi pet", "Kacamata hitam", "Tas anyaman"],
            "wanita": ["Topi jerami", "Kacamata hitam", "Tas anyaman"]
        },
        "kategori": "kasual",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kaos katun", "bobot": 0.35},
                    {"item": "Kemeja linen", "bobot": 0.3},
                    {"item": "Tank top kasual", "bobot": 0.25},
                    {"item": "Kaos santai", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana pendek cargo", "bobot": 0.35},
                    {"item": "Celana pendek denim", "bobot": 0.3},
                    {"item": "Celana pendek kasual", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Topi pet", "bobot": 0.3},
                    {"item": "Kacamata hitam", "bobot": 0.25},
                    {"item": "Tas anyaman", "bobot": 0.2},
                    {"item": "Sandal outdoor", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Dress santai", "bobot": 0.4},
                    {"item": "Kaos katun", "bobot": 0.3},
                    {"item": "Blouse santai", "bobot": 0.25},
                    {"item": "Tank top kasual", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Rok pendek", "bobot": 0.35},
                    {"item": "Celana pendek kasual", "bobot": 0.3},
                    {"item": "Celana jeans", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Topi jerami", "bobot": 0.3},
                    {"item": "Kacamata hitam", "bobot": 0.25},
                    {"item": "Tas anyaman", "bobot": 0.2},
                    {"item": "Sepatu kets", "bobot": 0.25}
                ]
            }
        }
    },
    "bandara": {
        "deskripsi": {
            "pria": "Hoodie nyaman, celana training dengan saku, sneakers, ransel traveling.",
            "wanita": "Sweater longgar, legging nyaman, sepatu kets, ransel kecil, syal besar."
        },
        "aksesori": {
            "pria": ["Ransel", "Kacamata hitam", "Syal"],
            "wanita": ["Ransel kecil", "Syal besar", "Kacamata hitam"]
        },
        "kategori": "kasual",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Hoodie nyaman", "bobot": 0.35},
                    {"item": "Kaos santai", "bobot": 0.3},
                    {"item": "Sweater crew neck", "bobot": 0.25},
                    {"item": "Jaket kasual", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana training", "bobot": 0.35},
                    {"item": "Celana jeans", "bobot": 0.3},
                    {"item": "Celana jogger", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Ransel", "bobot": 0.3},
                    {"item": "Kacamata hitam", "bobot": 0.25},
                    {"item": "Syal", "bobot": 0.2},
                    {"item": "Sneakers", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Sweater longgar", "bobot": 0.35},
                    {"item": "Kaos santai", "bobot": 0.3},
                    {"item": "Hoodie oversized", "bobot": 0.25},
                    {"item": "Blouse kasual", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Legging nyaman", "bobot": 0.35},
                    {"item": "Celana jeans", "bobot": 0.3},
                    {"item": "Celana jogger", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Ransel kecil", "bobot": 0.3},
                    {"item": "Syal besar", "bobot": 0.25},
                    {"item": "Kacamata hitam", "bobot": 0.2},
                    {"item": "Sepatu kets", "bobot": 0.25}
                ]
            }
        }
    },
    "cafe": {
        "deskripsi": {
            "pria": "Kemeja kasual lengan pendek, celana chino, sepatu loafers, jam tangan.",
            "wanita": "Sweater tipis, celana jeans skinny, sepatu kets, tas selempang kecil."
        },
        "aksesori": {
            "pria": ["Jam tangan", "Tas selempang", "Kacamata hitam"],
            "wanita": ["Tas selempang", "Kacamata hitam", "Jam tangan"]
        },
        "kategori": "kasual",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kemeja lengan pendek", "bobot": 0.35},
                    {"item": "Kaos santai", "bobot": 0.3},
                    {"item": "Sweater crew neck", "bobot": 0.25},
                    {"item": "Kemeja kasual", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana chino", "bobot": 0.35},
                    {"item": "Celana jeans", "bobot": 0.3},
                    {"item": "Celana jogger", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Jam tangan", "bobot": 0.3},
                    {"item": "Tas selempang", "bobot": 0.25},
                    {"item": "Kacamata hitam", "bobot": 0.2},
                    {"item": "Sepatu loafers", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Sweater tipis", "bobot": 0.35},
                    {"item": "Kaos santai", "bobot": 0.3},
                    {"item": "Blouse kasual", "bobot": 0.25},
                    {"item": "Kemeja oversized", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana jeans skinny", "bobot": 0.35},
                    {"item": "Celana kulot", "bobot": 0.3},
                    {"item": "Rok denim", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Tas selempang", "bobot": 0.3},
                    {"item": "Kacamata hitam", "bobot": 0.25},
                    {"item": "Jam tangan", "bobot": 0.2},
                    {"item": "Sepatu kets", "bobot": 0.25}
                ]
            }
        }
    },
    "perpustakaan": {
        "deskripsi": {
            "pria": "Kemeja flanel kasual, celana jeans, sepatu kets, cardigan ringan.",
            "wanita": "Cardigan panjang, kaos polos, celana jeans, sepatu flat, tas tote."
        },
        "aksesori": {
            "pria": ["Tote bag", "Kacamata baca", "Syal ringan"],
            "wanita": ["Tote bag", "Kacamata baca", "Syal ringan"]
        },
        "kategori": "kasual",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kemeja flanel", "bobot": 0.35},
                    {"item": "Kaos polos", "bobot": 0.3},
                    {"item": "Cardigan ringan", "bobot": 0.25},
                    {"item": "Sweater crew neck", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana jeans", "bobot": 0.35},
                    {"item": "Celana chino", "bobot": 0.3},
                    {"item": "Celana jogger", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Tote bag", "bobot": 0.3},
                    {"item": "Kacamata baca", "bobot": 0.25},
                    {"item": "Syal ringan", "bobot": 0.2},
                    {"item": "Sepatu kets", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Cardigan panjang", "bobot": 0.35},
                    {"item": "Kaos polos", "bobot": 0.3},
                    {"item": "Blouse santai", "bobot": 0.25},
                    {"item": "Sweater tipis", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana jeans", "bobot": 0.35},
                    {"item": "Celana kulot", "bobot": 0.3},
                    {"item": "Rok denim", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Tote bag", "bobot": 0.3},
                    {"item": "Kacamata baca", "bobot": 0.25},
                    {"item": "Syal ringan", "bobot": 0.2},
                    {"item": "Sepatu flat", "bobot": 0.25}
                ]
            }
        }
    },
    "hiking": {
        "deskripsi": {
            "pria": "Jaket outdoor tahan angin, kaos quick-dry, celana trekking, sepatu hiking, topi rimba.",
            "wanita": "Jaket softshell, legging hiking, kaos teknis, sepatu hiking, topi visor."
        },
        "aksesori": {
            "pria": ["Topi rimba", "Ransel hiking", "Tongkat hiking"],
            "kasual": ["Topi visor", "Ransel hiking", "Tongkat hiking"]
        },
        "kategori": "outdoor",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Jaket outdoor", "bobot": 0.4},
                    {"item": "Kaos quick-dry", "bobot": 0.35},
                    {"item": "Kaos teknis", "bobot": 0.3},
                    {"item": "Hoodie tahan air", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Celana trekking", "bobot": 0.4},
                    {"item": "Celana cargo", "bobot": 0.35},
                    {"item": "Celana pendek hiking", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Topi rimba", "bobot": 0.3},
                    {"item": "Ransel hiking", "bobot": 0.25},
                    {"item": "Tongkat hiking", "bobot": 0.2},
                    {"item": "Sepatu hiking", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Jaket softshell", "bobot": 0.4},
                    {"item": "Kaos teknis", "bobot": 0.35},
                    {"item": "Tank top olahraga", "bobot": 0.3},
                    {"item": "Hoodie outdoor", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Legging hiking", "bobot": 0.35},
                    {"item": "Celana trekking", "bobot": 0.3},
                    {"item": "Celana pendek hiking", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Topi visor", "bobot": 0.3},
                    {"item": "Ransel hiking", "bobot": 0.25},
                    {"item": "Tongkat hiking", "bobot": 0.2},
                    {"item": "Sepatu hiking", "bobot": 0.25}
                ]
            }
        }
    },
    "piknik": {
    "deskripsi": {
        "pria": "Kaos santai, celana pendek linen, sandal outdoor, topi pet.",
        "wanita": "Dress santai dengan motif floral, sandal jepit, topi jerami, kacamata hitam."
        },
        "aksesori": {
            "pria": ["Topi pet", "Keranjang piknik", "Kacamata hitam"],
            "wanita": ["Topi jerami", "Keranjang piknik", "Kacamata hitam"]
        },
        "kategori": "kasual",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kaos santai", "bobot": 0.35},
                    {"item": "Kemeja linen", "bobot": 0.3},
                    {"item": "Tank top kasual", "bobot": 0.25},
                    {"item": "Kaos katun", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana pendek linen", "bobot": 0.35},
                    {"item": "Celana pendek denim", "bobot": 0.3},
                    {"item": "Celana pendek kasual", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Topi pet", "bobot": 0.3},
                    {"item": "Keranjang piknik", "bobot": 0.25},
                    {"item": "Kacamata hitam", "bobot": 0.2},
                    {"item": "Sandal outdoor", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Dress santai floral", "bobot": 0.4},
                    {"item": "Kaos santai", "bobot": 0.3},
                    {"item": "Blouse kasual", "bobot": 0.25},
                    {"item": "Tank top katun", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Rok pendek", "bobot": 0.35},
                    {"item": "Celana pendek kasual", "bobot": 0.3},
                    {"item": "Celana jeans", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Topi jerami", "bobot": 0.3},
                    {"item": "Keranjang piknik", "bobot": 0.25},
                    {"item": "Kacamata hitam", "bobot": 0.2},
                    {"item": "Sandal jepit", "bobot": 0.25}
                ]
            }
        }
    },
    "acara keluarga": {
    "deskripsi": {
        "pria": "Batik modern lengan panjang, celana bahan slim-fit, sepatu loafers.",
        "wanita": "Kebaya modern dengan rok batik, sandal hak rendah, tas kecil."
        },
        "aksesori": {
            "pria": ["Jam tangan", "Ikat pinggang kulit", "Kacamata formal"],
            "wanita": ["Tas kecil", "Anting minimalis", "Jam tangan"]
        },
        "kategori": "semi-formal",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Batik modern", "bobot": 0.4},
                    {"item": "Kemeja lengan panjang", "bobot": 0.35},
                    {"item": "Kemeja batik", "bobot": 0.3},
                    {"item": "Kemeja formal", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Celana bahan slim-fit", "bobot": 0.4},
                    {"item": "Celana chino", "bobot": 0.35},
                    {"item": "Celana formal", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Jam tangan", "bobot": 0.3},
                    {"item": "Ikat pinggang kulit", "bobot": 0.25},
                    {"item": "Kacamata formal", "bobot": 0.2},
                    {"item": "Sepatu loafers", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Kebaya modern", "bobot": 0.4},
                    {"item": "Blouse elegan", "bobot": 0.35},
                    {"item": "Atasan batik", "bobot": 0.3},
                    {"item": "Kemeja sutra", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Rok batik", "bobot": 0.4},
                    {"item": "Rok midi", "bobot": 0.35},
                    {"item": "Celana bahan", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Tas kecil", "bobot": 0.3},
                    {"item": "Anting minimalis", "bobot": 0.25},
                    {"item": "Jam tangan", "bobot": 0.2},
                    {"item": "Sandal hak rendah", "bobot": 0.25}
                ]
            }
        }
    },
    "gym": {
    "deskripsi": {
        "pria": "Tank top olahraga, celana training dengan saku, sepatu gym, handuk kecil.",
        "wanita": "Sports bra, tank top olahraga, legging gym, sepatu gym, ikat rambut."
        },
        "aksesori": {
            "pria": ["Handuk kecil", "Botol air", "Sarung tangan gym"],
            "wanita": ["Ikat rambut", "Botol air", "Sarung tangan gym"]
        },
        "kategori": "olahraga",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Tank top olahraga", "bobot": 0.4},
                    {"item": "Kaos dry-fit", "bobot": 0.35},
                    {"item": "Kaos teknis", "bobot": 0.3},
                    {"item": "Hoodie olahraga", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Celana training", "bobot": 0.4},
                    {"item": "Celana pendek olahraga", "bobot": 0.35},
                    {"item": "Celana jogger olahraga", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Handuk kecil", "bobot": 0.3},
                    {"item": "Botol air", "bobot": 0.25},
                    {"item": "Sarung tangan gym", "bobot": 0.2},
                    {"item": "Sepatu gym", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Sports bra", "bobot": 0.4},
                    {"item": "Tank top olahraga", "bobot": 0.35},
                    {"item": "Kaos dry-fit", "bobot": 0.3},
                    {"item": "Hoodie olahraga", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Legging gym", "bobot": 0.4},
                    {"item": "Celana pendek olahraga", "bobot": 0.35},
                    {"item": "Celana jogger olahraga", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Ikat rambut", "bobot": 0.3},
                    {"item": "Botol air", "bobot": 0.25},
                    {"item": "Sarung tangan gym", "bobot": 0.2},
                    {"item": "Sepatu gym", "bobot": 0.25}
                ]
            }
        }
    },
    "reuni": {
    "deskripsi": {
        "pria": "Kemeja kasual dengan lengan digulung, celana chino, sepatu loafers.",
        "wanita": "Dress semi-formal selutut, sepatu flat, cardigan tipis."
        },
        "aksesori": {
            "pria": ["Jam tangan", "Tas selempang", "Kacamata hitam"],
            "wanita": ["Tas selempang", "Kacamata hitam", "Jam tangan"]
        },
        "kategori": "semi-formal",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kemeja kasual", "bobot": 0.35},
                    {"item": "Kemeja slim-fit", "bobot": 0.3},
                    {"item": "Blazer kasual", "bobot": 0.25},
                    {"item": "Kaos polo", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana chino", "bobot": 0.35},
                    {"item": "Celana bahan", "bobot": 0.3},
                    {"item": "Celana jeans slim-fit", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Jam tangan", "bobot": 0.3},
                    {"item": "Tas selempang", "bobot": 0.25},
                    {"item": "Kacamata hitam", "bobot": 0.2},
                    {"item": "Sepatu loafers", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Dress semi-formal", "bobot": 0.4},
                    {"item": "Cardigan tipis", "bobot": 0.35},
                    {"item": "Blouse elegan", "bobot": 0.3},
                    {"item": "Kemeja kasual", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Rok selutut", "bobot": 0.4},
                    {"item": "Celana bahan", "bobot": 0.35},
                    {"item": "Rok A-line", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Tas selempang", "bobot": 0.3},
                    {"item": "Kacamata hitam", "bobot": 0.25},
                    {"item": "Jam tangan", "bobot": 0.2},
                    {"item": "Sepatu flat", "bobot": 0.25}
                ]
            }
        }
    },
    "meeting": {
    "deskripsi": {
        "pria": "Kemeja formal lengan panjang, celana bahan tailored, sepatu kulit, jas blazer.",
        "wanita": "Blazer formal, kemeja sutra, celana bahan tailored, sepatu hak rendah, tas kerja."
        },
        "aksesori": {
            "pria": ["Tas kerja", "Jam tangan", "Kacamata formal"],
            "wanita": ["Tas kerja", "Jam tangan", "Kacamata formal"]
        },
        "kategori": "formal",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kemeja formal", "bobot": 0.4},
                    {"item": "Jas blazer", "bobot": 0.35},
                    {"item": "Kemeja lengan panjang", "bobot": 0.3},
                    {"item": "Vest formal", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Celana bahan tailored", "bobot": 0.4},
                    {"item": "Celana formal", "bobot": 0.35},
                    {"item": "Celana chino", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Tas kerja", "bobot": 0.3},
                    {"item": "Jam tangan", "bobot": 0.25},
                    {"item": "Kacamata formal", "bobot": 0.2},
                    {"item": "Sepatu kulit", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Blazer formal", "bobot": 0.4},
                    {"item": "Kemeja sutra", "bobot": 0.35},
                    {"item": "Blouse formal", "bobot": 0.3},
                    {"item": "Kemeja lengan panjang", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Celana bahan tailored", "bobot": 0.4},
                    {"item": "Rok pensil", "bobot": 0.35},
                    {"item": "Celana formal", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Tas kerja", "bobot": 0.3},
                    {"item": "Jam tangan", "bobot": 0.25},
                    {"item": "Kacamata formal", "bobot": 0.2},
                    {"item": "Sepatu hak rendah", "bobot": 0.25}
                ]
            }
        }
    },
    "olahraga": {
    "deskripsi": {
        "pria": "Kaos olahraga dry-fit, celana training longgar, sepatu lari, topi olahraga.",
        "wanita": "Tank top olahraga, legging training, sepatu lari, ikat rambut."
        },
        "aksesori": {
            "pria": ["Topi olahraga", "Botol air", "Smartwatch"],
            "wanita": ["Ikat rambut", "Botol air", "Smartwatch"]
        },
        "kategori": "olahraga",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kaos dry-fit", "bobot": 0.4},
                    {"item": "Tank top olahraga", "bobot": 0.35},
                    {"item": "Kaos teknis", "bobot": 0.3},
                    {"item": "Hoodie olahraga", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Celana training longgar", "bobot": 0.4},
                    {"item": "Celana pendek olahraga", "bobot": 0.35},
                    {"item": "Celana jogger olahraga", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Topi olahraga", "bobot": 0.3},
                    {"item": "Botol air", "bobot": 0.25},
                    {"item": "Smartwatch", "bobot": 0.2},
                    {"item": "Sepatu lari", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Tank top olahraga", "bobot": 0.4},
                    {"item": "Sports bra", "bobot": 0.35},
                    {"item": "Kaos dry-fit", "bobot": 0.3},
                    {"item": "Hoodie olahraga", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Legging training", "bobot": 0.4},
                    {"item": "Celana pendek olahraga", "bobot": 0.35},
                    {"item": "Celana jogger olahraga", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Ikat rambut", "bobot": 0.3},
                    {"item": "Botol air", "bobot": 0.25},
                    {"item": "Smartwatch", "bobot": 0.2},
                    {"item": "Sepatu lari", "bobot": 0.25}
                ]
            }
        }
    },
    "seminar": {
    "deskripsi": {
        "pria": "Kemeja formal dengan lengan digulung, celana bahan, sepatu loafers, blazer opsional.",
        "wanita": "Kemeja formal, rok bahan selutut, sepatu hak rendah, blazer ringan."
        },
        "aksesori": {
            "pria": ["Tas kerja", "Jam tangan", "Kacamata baca"],
            "wanita": ["Tas kerja", "Jam tangan", "Kacamata baca"]
        },
        "kategori": "formal",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kemeja formal", "bobot": 0.4},
                    {"item": "Blazer opsional", "bobot": 0.35},
                    {"item": "Kemeja lengan panjang", "bobot": 0.3},
                    {"item": "Kemeja slim-fit", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Celana bahan", "bobot": 0.4},
                    {"item": "Celana chino", "bobot": 0.35},
                    {"item": "Celana formal", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Tas kerja", "bobot": 0.3},
                    {"item": "Jam tangan", "bobot": 0.25},
                    {"item": "Kacamata baca", "bobot": 0.2},
                    {"item": "Sepatu loafers", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Kemeja formal", "bobot": 0.4},
                    {"item": "Blazer ringan", "bobot": 0.35},
                    {"item": "Blouse elegan", "bobot": 0.3},
                    {"item": "Kemeja sutra", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Rok bahan selutut", "bobot": 0.4},
                    {"item": "Celana bahan", "bobot": 0.35},
                    {"item": "Rok midi", "bobot": 0.3}
                ],
                "aksesori": [
                    {"item": "Tas kerja", "bobot": 0.3},
                    {"item": "Jam tangan", "bobot": 0.25},
                    {"item": "Kacamata baca", "bobot": 0.2},
                    {"item": "Sepatu hak rendah", "bobot": 0.25}
                ]
            }
        }
    },
    "acara sosial": {
    "deskripsi": {
        "pria": "Kaos kasual dengan motif simpel, celana jeans, sepatu kets.",
        "wanita": "Dress santai dengan motif floral, sandal flat, cardigan tipis."
        },
        "aksesori": {
            "pria": ["Tas selempang", "Kacamata hitam", "Gelang simpel"],
            "wanita": ["Tas selempang", "Kacamata hitam", "Gelang simpel"]
        },
        "kategori": "kasual",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kaos kasual", "bobot": 0.35},
                    {"item": "Kemeja kasual", "bobot": 0.3},
                    {"item": "Sweater crew neck", "bobot": 0.25},
                    {"item": "Hoodie simpel", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana jeans", "bobot": 0.35},
                    {"item": "Celana chino", "bobot": 0.3},
                    {"item": "Celana jogger", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Tas selempang", "bobot": 0.3},
                    {"item": "Kacamata hitam", "bobot": 0.25},
                    {"item": "Gelang simpel", "bobot": 0.2},
                    {"item": "Sepatu kets", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Dress santai floral", "bobot": 0.4},
                    {"item": "Cardigan tipis", "bobot": 0.35},
                    {"item": "Kaos kasual", "bobot": 0.3},
                    {"item": "Blouse santai", "bobot": 0.25}
                ],
                "bawahan": [
                    {"item": "Rok pendek", "bobot": 0.35},
                    {"item": "Celana jeans", "bobot": 0.3},
                    {"item": "Celana kulot", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Tas selempang", "bobot": 0.3},
                    {"item": "Kacamata hitam", "bobot": 0.25},
                    {"item": "Gelang simpel", "bobot": 0.2},
                    {"item": "Sandal flat", "bobot": 0.25}
                ]
            }
        }
    },
    "event musik": {
    "deskripsi": {
        "pria": "Kaos band dengan grafis, celana jeans ripped, sepatu sneakers, jaket bomber.",
        "wanita": "Tank top edgy, celana jeans high-waist, sepatu boots, jaket kulit."
        },
        "aksesori": {
            "pria": ["Gelang kulit", "Topi baseball", "Tas pinggang"],
            "wanita": ["Gelang kulit", "Topi baseball", "Tas pinggang"]
        },
        "kategori": "kasual",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kaos band", "bobot": 0.35},
                    {"item": "Kaos edgy", "bobot": 0.3},
                    {"item": "Jaket bomber", "bobot": 0.25},
                    {"item": "Hoodie simpel", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana jeans ripped", "bobot": 0.35},
                    {"item": "Celana jeans slim-fit", "bobot": 0.3},
                    {"item": "Celana jogger", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Gelang kulit", "bobot": 0.25},
                    {"item": "Topi baseball", "bobot": 0.3},
                    {"item": "Tas pinggang", "bobot": 0.2},
                    {"item": "Sepatu sneakers", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Tank top edgy", "bobot": 0.35},
                    {"item": "Kaos grafis", "bobot": 0.3},
                    {"item": "Jaket kulit", "bobot": 0.25},
                    {"item": "Sweater crop", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana jeans high-waist", "bobot": 0.35},
                    {"item": "Celana jeans ripped", "bobot": 0.3},
                    {"item": "Rok denim", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Gelang kulit", "bobot": 0.25},
                    {"item": "Topi baseball", "bobot": 0.3},
                    {"item": "Tas pinggang", "bobot": 0.2},
                    {"item": "Sepatu boots", "bobot": 0.25}
                ]
            }
        }
    },
    "workshop": {
    "deskripsi": {
        "pria": "Kemeja kasual dengan lengan digulung, celana chino, sepatu loafers, tas laptop.",
        "wanita": "Kaos polos dengan blazer ringan, celana jeans, sepatu flat, tas tote."
        },
        "aksesori": {
            "pria": ["Tas laptop", "Kacamata baca", "Jam tangan"],
            "wanita": ["Tas tote", "Kacamata baca", "Jam tangan"]
        },
        "kategori": "kasual",
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kemeja kasual", "bobot": 0.35},
                    {"item": "Kaos polos", "bobot": 0.3},
                    {"item": "Blazer kasual", "bobot": 0.25},
                    {"item": "Sweater crew neck", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana chino", "bobot": 0.35},
                    {"item": "Celana jeans", "bobot": 0.3},
                    {"item": "Celana jogger", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Tas laptop", "bobot": 0.3},
                    {"item": "Kacamata baca", "bobot": 0.25},
                    {"item": "Jam tangan", "bobot": 0.2},
                    {"item": "Sepatu loafers", "bobot": 0.25}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Kaos polos", "bobot": 0.35},
                    {"item": "Blazer ringan", "bobot": 0.3},
                    {"item": "Blouse kasual", "bobot": 0.25},
                    {"item": "Cardigan tipis", "bobot": 0.2}
                ],
                "bawahan": [
                    {"item": "Celana jeans", "bobot": 0.35},
                    {"item": "Celana kulot", "bobot": 0.3},
                    {"item": "Rok denim", "bobot": 0.25}
                ],
                "aksesori": [
                    {"item": "Tas tote", "bobot": 0.3},
                    {"item": "Kacamata baca", "bobot": 0.25},
                    {"item": "Jam tangan", "bobot": 0.2},
                    {"item": "Sepatu flat", "bobot": 0.25}
                ]
            }
        }
    },
}

event_list = list(outfit_rekomendasi.keys())

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
        selected_items = request.form.getlist('items')  # Ambil item yang dicentang
        if not event or event not in outfit_rekomendasi or gender not in ['pria', 'wanita']:
            return render_template('final.html', 
                                 event="Tidak ditemukan",
                                 deskripsi="Maaf, acara atau gender tidak ditemukan.",
                                 aksesori=[],
                                 kategori="",
                                 kecocokan=0,
                                 selected_items=[])

        # Validasi: pastikan minimal satu item per kategori
        checklist = outfit_rekomendasi[event]['checklist'][gender]
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

        # Hitung skor kecocokan
        total_bobot = 0
        max_bobot = sum(item['bobot'] for cat in checklist.values() for item in cat)
        for item in selected_items:
            for category in checklist.values():
                for checklist_item in category:
                    if checklist_item['item'] == item:
                        total_bobot += checklist_item['bobot']

        kecocokan = (total_bobot / max_bobot) * 100 if max_bobot > 0 else 0
        kecocokan = round(min(kecocokan, 100), 2)  # Batasi maksimum 100%

        data = outfit_rekomendasi[event]
        deskripsi = data['deskripsi'][gender]
        aksesori = data['aksesori'][gender]
        return render_template('final.html', 
                             event=event.capitalize(),
                             deskripsi=deskripsi,
                             aksesori=aksesori,
                             kategori=data['kategori'],
                             kecocokan=kecocokan,
                             selected_items=selected_items,
                             gender=gender)
    
    event = request.args.get('event', '').lower()
    gender = request.args.get('gender', '').lower()
    if not event or event not in outfit_rekomendasi or gender not in ['pria', 'wanita']:
        return render_template('final.html', 
                             event="Tidak ditemukan",
                             deskripsi="Maaf, acara atau gender tidak ditemukan.",
                             aksesori=[],
                             kategori="",
                             kecocokan=0,
                             selected_items=[])
    
    data = outfit_rekomendasi[event]
    deskripsi = data['deskripsi'][gender]
    aksesori = data['aksesori'][gender]
    return render_template('final.html', 
                         event=event.capitalize(),
                         deskripsi=deskripsi,
                         aksesori=aksesori,
                         kategori=data['kategori'],
                         kecocokan=100,
                         selected_items=[],
                         gender=gender)

@app.route('/search', methods=['POST'])
def search_event():
    query = request.form.get('event_input', '').lower().strip()
    if not query:
        return jsonify({"error": "Masukkan nama acara."})

    best_match = None
    highest_score = 0
    for event in event_list:
        score = fuzz.partial_ratio(query, event)
        if score > highest_score and score > 70:
            highest_score = score
            best_match = event

    if best_match:
        data = outfit_rekomendasi[best_match]
        return jsonify({
            "event": best_match.capitalize(),
            "deskripsi_pria": data['deskripsi']['pria'],
            "deskripsi_wanita": data['deskripsi']['wanita'],
            "kategori": data['kategori'],
            "checklist": data['checklist']
        })
    return jsonify({"error": "Acara tidak ditemukan. Coba kata kunci lain."})

if __name__ == "__main__":
    app.run(debug=True)