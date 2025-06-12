# Data rekomendasi outfit dengan checklist spesifik gender
outfit_rekomendasi = {
    "kuliah": {
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kemeja flanel lengan panjang", "bobot": 3},
                    {"item": "Kemeja lengan pendek", "bobot": 2},
                    {"item": "Kaos polo", "bobot": 1},
                    {"item": "Sweater crew neck", "bobot": 1}
                ],
                "bawahan": [
                    {"item": "Celana kain", "bobot": 3},
                    {"item": "Celana chinos", "bobot": 2},
                    {"item": "Celana jeans", "bobot": 1}
                ],
                "aksesori": [
                    {"item": "Ransel", "bobot": 4},
                    {"item": "Sepatu", "bobot": 3},
                    {"item": "Sabuk", "bobot": 2},
                    {"item": "Kacamata", "bobot": 1},
                    {"item": "Jam tangan", "bobot": 1}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Blouse kasual", "bobot": 3},
                    {"item": "Kemeja lengan pendek", "bobot": 2},
                    {"item": "Kaos nyaman", "bobot": 1},
                    {"item": "Cardigan tipis", "bobot": 1}
                ],
                "bawahan": [
                    {"item": "Celana kulot", "bobot": 3},
                    {"item": "Celana jeans skinny", "bobot": 2},
                    {"item": "Rok denim", "bobot": 1}
                ],
                "aksesori": [
                    {"item": "Tote bag", "bobot": 4},
                    {"item": "Sepatu flat", "bobot": 3},
                    {"item": "Syal ringan", "bobot": 2},
                    {"item": "Kacamata baca", "bobot": 1},
                    {"item": "Gelang simpel", "bobot": 1}
                ]
            }
        },
        "aturan": {
            "pria": [
                {
                    "nama": "Formal Kuliah",
                    "kombinasi": ["Kemeja flanel lengan panjang", "Celana kain", "Sepatu", "Ransel"],
                    "deskripsi": "Tampilan formal untuk presentasi atau kuliah penting",
                    "bobot_min": 10,
                    "confidence_base": 90
                },
                {
                    "nama": "Smart Casual",
                    "kombinasi": ["Kemeja lengan pendek", "Celana chinos", "Sepatu", "Ransel"],
                    "deskripsi": "Tampilan rapi namun santai untuk kuliah sehari-hari",
                    "bobot_min": 7,
                    "confidence_base": 80
                },
                {
                    "nama": "Casual Kuliah",
                    "kombinasi": ["Kaos polo", "Celana jeans", "Sepatu", "Ransel"],
                    "deskripsi": "Tampilan santai untuk suasana kampus yang rileks",
                    "bobot_min": 4,
                    "confidence_base": 70
                }
            ],
            "wanita": [
                {
                    "nama": "Formal Kuliah",
                    "kombinasi": ["Blouse kasual", "Celana kulot", "Sepatu flat", "Tote bag"],
                    "deskripsi": "Tampilan formal untuk presentasi atau kuliah penting",
                    "bobot_min": 10,
                    "confidence_base": 90
                },
                {
                    "nama": "Smart Casual",
                    "kombinasi": ["Kemeja lengan pendek", "Celana jeans skinny", "Sepatu flat", "Tote bag"],
                    "deskripsi": "Tampilan rapi namun santai untuk kuliah sehari-hari",
                    "bobot_min": 7,
                    "confidence_base": 80
                },
                {
                    "nama": "Casual Kuliah",
                    "kombinasi": ["Kaos nyaman", "Rok denim", "Sepatu flat", "Tote bag"],
                    "deskripsi": "Tampilan santai untuk suasana kampus yang rileks",
                    "bobot_min": 4,
                    "confidence_base": 70
                }
            ]
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
                    {"item": "Jas slim-fit", "bobot": 4},
                    {"item": "Kemeja putih", "bobot": 3},
                    {"item": "Batik modern", "bobot": 2},
                    {"item": "Kemeja formal", "bobot": 2},
                    {"item": "Vest formal", "bobot": 1}
                ],
                "bawahan": [
                    {"item": "Celana bahan", "bobot": 4},
                    {"item": "Celana formal", "bobot": 3},
                    {"item": "Celana tailored", "bobot": 2}
                ],
                "aksesori": [
                    {"item": "Dasi sutra", "bobot": 3},
                    {"item": "Jam tangan elegan", "bobot": 2},
                    {"item": "Ikat pinggang kulit", "bobot": 2},
                    {"item": "Sepatu kulit", "bobot": 3}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Gaun midi", "bobot": 4},
                    {"item": "Kebaya modern", "bobot": 3},
                    {"item": "Blouse elegan", "bobot": 2},
                    {"item": "Atasan renda", "bobot": 1}
                ],
                "bawahan": [
                    {"item": "Rok songket", "bobot": 4},
                    {"item": "Rok midi", "bobot": 3},
                    {"item": "Celana bahan", "bobot": 2},
                    {"item": "Rok A-line", "bobot": 1}
                ],
                "aksesori": [
                    {"item": "Clutch elegan", "bobot": 3},
                    {"item": "Sepatu hak tinggi", "bobot": 3},
                    {"item": "Anting minimalis", "bobot": 2},
                    {"item": "Kalung simpel", "bobot": 1}
                ]
            }
        },
        "aturan": {
            "pria": [
                {
                    "nama": "Formal Nikahan",
                    "kombinasi": ["Jas slim-fit", "Celana bahan", "Kemeja putih", "Dasi sutra", "Sepatu kulit"],
                    "deskripsi": "Tampilan formal lengkap untuk acara pernikahan",
                    "bobot_min": 15,
                    "confidence_base": 95
                },
                {
                    "nama": "Semi-Formal",
                    "kombinasi": ["Batik modern", "Celana formal", "Sepatu kulit"],
                    "deskripsi": "Tampilan elegan dengan sentuhan budaya",
                    "bobot_min": 7,
                    "confidence_base": 85
                }
            ],
            "wanita": [
                {
                    "nama": "Elegan Nikahan",
                    "kombinasi": ["Gaun midi", "Sepatu hak tinggi", "Clutch elegan"],
                    "deskripsi": "Tampilan anggun untuk acara pernikahan",
                    "bobot_min": 10,
                    "confidence_base": 95
                },
                {
                    "nama": "Tradisional Modern",
                    "kombinasi": ["Kebaya modern", "Rok songket", "Sepatu hak tinggi"],
                    "deskripsi": "Tampilan tradisional dengan nuansa modern",
                    "bobot_min": 10,
                    "confidence_base": 90
                }
            ]
        }
    },
    "pantai": {
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kaos linen", "bobot": 3},
                    {"item": "Kemeja pantai", "bobot": 2},
                    {"item": "Kaos tipis", "bobot": 1},
                    {"item": "Tank top kasual", "bobot": 1}
                ],
                "bawahan": [
                    {"item": "Celana pendek chino", "bobot": 3},
                    {"item": "Celana pendek denim", "bobot": 2},
                    {"item": "Celana pendek kasual", "bobot": 1}
                ],
                "aksesori": [
                    {"item": "Topi jerami", "bobot": 3},
                    {"item": "Kacamata hitam", "bobot": 2},
                    {"item": "Sandal jepit", "bobot": 2},
                    {"item": "Tote bag kanvas", "bobot": 1}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Maxi dress", "bobot": 4},
                    {"item": "Kaos tipis", "bobot": 2},
                    {"item": "Blouse pantai", "bobot": 2},
                    {"item": "Tank top kasual", "bobot": 1},
                    {"item": "Kemeja oversized", "bobot": 1}
                ],
                "bawahan": [
                    {"item": "Rok maxi", "bobot": 3},
                    {"item": "Celana pendek kasual", "bobot": 2},
                    {"item": "Celana palazzo", "bobot": 2},
                    {"item": "Rok pendek", "bobot": 1}
                ],
                "aksesori": [
                    {"item": "Topi pantai lebar", "bobot": 3},
                    {"item": "Kacamata hitam", "bobot": 2},
                    {"item": "Tote bag kanvas", "bobot": 2},
                    {"item": "Sandal jepit", "bobot": 2}
                ]
            }
        },
        "aturan": {
            "pria": [
                {
                    "nama": "Beach Casual",
                    "kombinasi": ["Kaos linen", "Celana pendek chino", "Sandal jepit", "Topi jerami"],
                    "deskripsi": "Tampilan santai dan nyaman untuk di pantai",
                    "bobot_min": 8,
                    "confidence_base": 90
                },
                {
                    "nama": "Relaxed Beach",
                    "kombinasi": ["Kaos tipis", "Celana pendek denim", "Sandal jepit"],
                    "deskripsi": "Tampilan minimalis untuk suasana pantai",
                    "bobot_min": 4,
                    "confidence_base": 80
                }
            ],
            "wanita": [
                {
                    "nama": "Bohemian Beach",
                    "kombinasi": ["Maxi dress", "Sandal jepit", "Topi pantai lebar"],
                    "deskripsi": "Tampilan flowy dan elegan untuk pantai",
                    "bobot_min": 9,
                    "confidence_base": 90
                },
                {
                    "nama": "Casual Beach",
                    "kombinasi": ["Kaos tipis", "Rok pendek", "Sandal jepit"],
                    "deskripsi": "Tampilan simpel untuk jalan-jalan di pantai",
                    "bobot_min": 4,
                    "confidence_base": 80
                }
            ]
        }
    },
    "kantor": {
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kemeja oxford", "bobot": 4},
                    {"item": "Kemeja formal", "bobot": 3},
                    {"item": "Blazer", "bobot": 3},
                    {"item": "Kemeja lengan panjang", "bobot": 2}
                ],
                "bawahan": [
                    {"item": "Celana chino tailored", "bobot": 4},
                    {"item": "Celana bahan", "bobot": 3},
                    {"item": "Celana formal", "bobot": 2}
                ],
                "aksesori": [
                    {"item": "Ikat pinggang kulit", "bobot": 3},
                    {"item": "Jam tangan klasik", "bobot": 2},
                    {"item": "Kacamata formal", "bobot": 1},
                    {"item": "Sepatu loafer formal", "bobot": 3}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Blazer terstruktur", "bobot": 4},
                    {"item": "Kemeja sutra", "bobot": 3},
                    {"item": "Blouse formal", "bobot": 2},
                    {"item": "Kemeja lengan panjang", "bobot": 2}
                ],
                "bawahan": [
                    {"item": "Rok pensil", "bobot": 4},
                    {"item": "Celana bahan tailored", "bobot": 3},
                    {"item": "Rok midi", "bobot": 2},
                    {"item": "Celana formal", "bobot": 2}
                ],
                "aksesori": [
                    {"item": "Tote bag kulit", "bobot": 3},
                    {"item": "Jam tangan klasik", "bobot": 2},
                    {"item": "Kacamata formal", "bobot": 1},
                    {"item": "Sepatu hak rendah", "bobot": 3}
                ]
            }
        },
        "aturan": {
            "pria": [
                {
                    "nama": "Business Formal",
                    "kombinasi": ["Kemeja oxford", "Celana chino tailored", "Blazer", "Sepatu loafer formal"],
                    "deskripsi": "Tampilan profesional untuk meeting penting",
                    "bobot_min": 12,
                    "confidence_base": 95
                },
                {
                    "nama": "Business Casual",
                    "kombinasi": ["Kemeja formal", "Celana bahan", "Ikat pinggang kulit"],
                    "deskripsi": "Tampilan rapi untuk kerja sehari-hari",
                    "bobot_min": 8,
                    "confidence_base": 85
                }
            ],
            "wanita": [
                {
                    "nama": "Business Formal",
                    "kombinasi": ["Blazer terstruktur", "Kemeja sutra", "Rok pensil", "Sepatu hak rendah"],
                    "deskripsi": "Tampilan profesional untuk meeting penting",
                    "bobot_min": 12,
                    "confidence_base": 95
                },
                {
                    "nama": "Business Casual",
                    "kombinasi": ["Blouse formal", "Celana bahan tailored", "Tote bag kulit"],
                    "deskripsi": "Tampilan rapi untuk kerja sehari-hari",
                    "bobot_min": 8,
                    "confidence_base": 85
                }
            ]
        }
    },
    "belanja": {
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Hoodie simpel", "bobot": 4},
                    {"item": "Kaos santai", "bobot": 3},
                    {"item": "Sweater crew neck", "bobot": 2},
                    {"item": "Kemeja kasual", "bobot": 1}
                ],
                "bawahan": [
                    {"item": "Celana jeans relaxed-fit", "bobot": 4},
                    {"item": "Celana jogger", "bobot": 3},
                    {"item": "Celana pendek kasual", "bobot": 2}
                ],
                "aksesori": [
                    {"item": "Topi snapback", "bobot": 3},
                    {"item": "Tas belanja kanvas", "bobot": 2},
                    {"item": "Kacamata hitam", "bobot": 1},
                    {"item": "Sneakers nyaman", "bobot": 2}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Kaos santai", "bobot": 4},
                    {"item": "Cardigan ringan", "bobot": 3},
                    {"item": "Blouse kasual", "bobot": 2},
                    {"item": "Sweater tipis", "bobot": 1}
                ],
                "bawahan": [
                    {"item": "Celana jeans", "bobot": 4},
                    {"item": "Celana kulot", "bobot": 3},
                    {"item": "Rok denim", "bobot": 2}
                ],
                "aksesori": [
                    {"item": "Tas belanja kanvas", "bobot": 3},
                    {"item": "Kacamata hitam", "bobot": 2},
                    {"item": "Topi snapback", "bobot": 1},
                    {"item": "Sepatu kets", "bobot": 2}
                ]
            }
        },
        "aturan": {
            "pria": [
                {
                    "nama": "Kasual Nyaman",
                    "kombinasi": ["Hoodie simpel", "Celana jeans relaxed-fit", "Sneakers nyaman", "Tas belanja kanvas"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Gaya santai dan praktis untuk berbelanja seharian."
                },
                {
                    "nama": "Kasual Stylish",
                    "kombinasi": ["Kaos santai", "Celana jogger", "Topi snapback", "Kacamata hitam"],
                    "bobot_min": 8,
                    "confidence_base": 80,
                    "deskripsi": "Tampilan kasual dengan sentuhan gaya untuk suasana belanja yang trendy."
                }
            ],
            "wanita": [
                {
                    "nama": "Kasual Chic",
                    "kombinasi": ["Kaos santai", "Cardigan ringan", "Celana jeans", "Sepatu kets"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Gaya santai namun tetap elegan untuk aktivitas belanja."
                },
                {
                    "nama": "Kasual Praktis",
                    "kombinasi": ["Blouse kasual", "Celana kulot", "Tas belanja kanvas", "Topi snapback"],
                    "bobot_min": 8,
                    "confidence_base": 80,
                    "deskripsi": "Kombinasi nyaman dan fungsional untuk berbelanja."
                }
            ]
        }
    },
    "makan malam": {
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kemeja slim-fit", "bobot": 5},
                    {"item": "Kemeja lengan panjang", "bobot": 4},
                    {"item": "Blazer kasual", "bobot": 3},
                    {"item": "Kemeja formal", "bobot": 2}
                ],
                "bawahan": [
                    {"item": "Celana bahan tailored", "bobot": 5},
                    {"item": "Celana chino", "bobot": 4},
                    {"item": "Celana formal", "bobot": 3}
                ],
                "aksesori": [
                    {"item": "Jam tangan elegan", "bobot": 3},
                    {"item": "Ikat pinggang kulit", "bobot": 2},
                    {"item": "Kacamata formal", "bobot": 1},
                    {"item": "Sepatu loafers", "bobot": 2}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Dress semi-formal", "bobot": 5},
                    {"item": "Blouse elegan", "bobot": 4},
                    {"item": "Kemeja sutra", "bobot": 3},
                    {"item": "Atasan ruffle", "bobot": 2}
                ],
                "bawahan": [
                    {"item": "Rok selutut", "bobot": 5},
                    {"item": "Celana bahan", "bobot": 4},
                    {"item": "Rok A-line", "bobot": 3}
                ],
                "aksesori": [
                    {"item": "Clutch", "bobot": 3},
                    {"item": "Jam tangan elegan", "bobot": 2},
                    {"item": "Anting kecil", "bobot": 1},
                    {"item": "Sepatu hak rendah", "bobot": 2}
                ]
            }
        },
        "aturan": {
            "pria": [
                {
                    "nama": "Semi-Formal Elegan",
                    "kombinasi": ["Kemeja slim-fit", "Celana bahan tailored", "Sepatu loafers", "Jam tangan elegan"],
                    "bobot_min": 12,
                    "confidence_base": 90,
                    "deskripsi": "Tampilan rapi dan elegan untuk makan malam formal."
                },
                {
                    "nama": "Smart Casual",
                    "kombinasi": ["Kemeja lengan panjang", "Celana chino", "Ikat pinggang kulit", "Kacamata formal"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Gaya semi-formal yang lebih santai namun tetap berkelas."
                }
            ],
            "wanita": [
                {
                    "nama": "Elegan Feminin",
                    "kombinasi": ["Dress semi-formal", "Sepatu hak rendah", "Clutch", "Anting kecil"],
                    "bobot_min": 12,
                    "confidence_base": 90,
                    "deskripsi": "Gaya anggun untuk suasana makan malam yang spesial."
                },
                {
                    "nama": "Semi-Formal Chic",
                    "kombinasi": ["Blouse elegan", "Rok selutut", "Jam tangan elegan", "Sepatu hak rendah"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Kombinasi elegan dengan sentuhan modern."
                }
            ]
        }
    },
    "bioskop": {
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Sweater crew neck", "bobot": 4},
                    {"item": "Kaos santai", "bobot": 3},
                    {"item": "Jaket denim", "bobot": 2},
                    {"item": "Hoodie simpel", "bobot": 1}
                ],
                "bawahan": [
                    {"item": "Celana jeans", "bobot": 4},
                    {"item": "Celana chino", "bobot": 3},
                    {"item": "Celana jogger", "bobot": 2}
                ],
                "aksesori": [
                    {"item": "Tas selempang", "bobot": 3},
                    {"item": "Syal ringan", "bobot": 1},
                    {"item": "Sneakers", "bobot": 2}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Hoodie oversized", "bobot": 4},
                    {"item": "Kaos santai", "bobot": 3},
                    {"item": "Sweater tipis", "bobot": 2},
                    {"item": "Blouse kasual", "bobot": 1}
                ],
                "bawahan": [
                    {"item": "Celana jeans skinny", "bobot": 4},
                    {"item": "Celana kulot", "bobot": 3},
                    {"item": "Rok denim", "bobot": 2}
                ],
                "aksesori": [
                    {"item": "Tas selempang", "bobot": 3},
                    {"item": "Syal ringan", "bobot": 1},
                    {"item": "Sepatu kets", "bobot": 2}
                ]
            }
        },
        "aturan": {
            "pria": [
                {
                    "nama": "Kasual Nyaman",
                    "kombinasi": ["Sweater crew neck", "Celana jeans", "Sneakers", "Tas selempang"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Gaya santai untuk menikmati film di bioskop."
                },
                {
                    "nama": "Kasual Stylish",
                    "kombinasi": ["Jaket denim", "Celana chino", "Syal ringan", "Sneakers"],
                    "bobot_min": 8,
                    "confidence_base": 80,
                    "deskripsi": "Tampilan kasual dengan sentuhan gaya untuk suasana bioskop."
                }
            ],
            "wanita": [
                {
                    "nama": "Kasual Chic",
                    "kombinasi": ["Hoodie oversized", "Celana jeans skinny", "Sepatu kets", "Tas selempang"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Gaya santai namun tetap stylish untuk ke bioskop."
                },
                {
                    "nama": "Kasual Praktis",
                    "kombinasi": ["Sweater tipis", "Celana kulot", "Syal ringan", "Kacamata hitam"],
                    "bobot_min": 8,
                    "confidence_base": 80,
                    "deskripsi": "Kombinasi nyaman untuk menonton film."
                }
            ]
        }
    },
    "taman": {
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kaos katun", "bobot": 4},
                    {"item": "Kemeja linen", "bobot": 3},
                    {"item": "Tank top kasual", "bobot": 2},
                    {"item": "Kaos santai", "bobot": 1}
                ],
                "bawahan": [
                    {"item": "Celana pendek cargo", "bobot": 4},
                    {"item": "Celana pendek denim", "bobot": 3},
                    {"item": "Celana pendek kasual", "bobot": 2}
                ],
                "aksesori": [
                    {"item": "Topi pet", "bobot": 3},
                    {"item": "Kacamata hitam", "bobot": 2},
                    {"item": "Tas anyaman", "bobot": 1},
                    {"item": "Sandal outdoor", "bobot": 2}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Dress santai", "bobot": 5},
                    {"item": "Kaos katun", "bobot": 3},
                    {"item": "Blouse santai", "bobot": 2},
                    {"item": "Tank top kasual", "bobot": 1}
                ],
                "bawahan": [
                    {"item": "Rok pendek", "bobot": 4},
                    {"item": "Celana pendek kasual", "bobot": 3},
                    {"item": "Celana jeans", "bobot": 2}
                ],
                "aksesori": [
                    {"item": "Topi jerami", "bobot": 3},
                    {"item": "Kacamata hitam", "bobot": 2},
                    {"item": "Tas anyaman", "bobot": 1},
                    {"item": "Sepatu kets", "bobot": 2}
                ]
            }
        },
        "aturan": {
            "pria": [
                {
                    "nama": "Kasual Outdoor",
                    "kombinasi": ["Kaos katun", "Celana pendek cargo", "Sandal outdoor", "Topi pet"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Gaya santai dan nyaman untuk bersantai di taman."
                },
                {
                    "nama": "Kasual Praktis",
                    "kombinasi": ["Kemeja linen", "Celana pendek denim", "Kacamata hitam", "Tas anyaman"],
                    "bobot_min": 8,
                    "confidence_base": 80,
                    "deskripsi": "Tampilan kasual untuk aktivitas luar ruangan."
                }
            ],
            "wanita": [
                {
                    "nama": "Kasual Feminin",
                    "kombinasi": ["Dress santai", "Sepatu kets", "Topi jerami", "Tas anyaman"],
                    "bobot_min": 12,
                    "confidence_base": 85,
                    "deskripsi": "Gaya santai dengan sentuhan feminin untuk di taman."
                },
                {
                    "nama": "Kasual Nyaman",
                    "kombinasi": ["Kaos katun", "Rok pendek", "Kacamata hitam", "Sepatu kets"],
                    "bobot_min": 8,
                    "confidence_base": 80,
                    "deskripsi": "Kombinasi praktis untuk hari santai di taman."
                }
            ]
        }
    },
    "bandara": {
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Hoodie nyaman", "bobot": 4},
                    {"item": "Kaos santai", "bobot": 3},
                    {"item": "Sweater crew neck", "bobot": 2},
                    {"item": "Jaket kasual", "bobot": 1}
                ],
                "bawahan": [
                    {"item": "Celana training", "bobot": 4},
                    {"item": "Celana jeans", "bobot": 3},
                    {"item": "Celana jogger", "bobot": 2}
                ],
                "aksesori": [
                    {"item": "Ransel", "bobot": 3},
                    {"item": "Kacamata hitam", "bobot": 2},
                    {"item": "Syal", "bobot": 1},
                    {"item": "Sneakers", "bobot": 2}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Sweater longgar", "bobot": 4},
                    {"item": "Kaos santai", "bobot": 3},
                    {"item": "Hoodie oversized", "bobot": 2},
                    {"item": "Blouse kasual", "bobot": 1}
                ],
                "bawahan": [
                    {"item": "Legging nyaman", "bobot": 4},
                    {"item": "Celana jeans", "bobot": 3},
                    {"item": "Celana jogger", "bobot": 2}
                ],
                "aksesori": [
                    {"item": "Ransel kecil", "bobot": 3},
                    {"item": "Syal besar", "bobot": 2},
                    {"item": "Kacamata hitam", "bobot": 1},
                    {"item": "Sepatu kets", "bobot": 2}
                ]
            }
        },
        "aturan": {
            "pria": [
                {
                    "nama": "Travel Kasual",
                    "kombinasi": ["Hoodie nyaman", "Celana training", "Sneakers", "Ransel"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Gaya nyaman untuk perjalanan di bandara."
                },
                {
                    "nama": "Travel Stylish",
                    "kombinasi": ["Sweater crew neck", "Celana jeans", "Syal", "Kacamata hitam"],
                    "bobot_min": 8,
                    "confidence_base": 80,
                    "deskripsi": "Tampilan kasual dengan gaya untuk bepergian."
                }
            ],
            "wanita": [
                {
                    "nama": "Travel Chic",
                    "kombinasi": ["Sweater longgar", "Legging nyaman", "Sepatu kets", "Ransel kecil"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Gaya santai namun chic untuk di bandara."
                },
                {
                    "nama": "Travel Praktis",
                    "kombinasi": ["Hoodie oversized", "Celana jogger", "Syal besar", "Kacamata hitam"],
                    "bobot_min": 8,
                    "confidence_base": 80,
                    "deskripsi": "Kombinasi nyaman untuk perjalanan jauh."
                }
            ]
        }
    },
    "cafe": {
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kemeja lengan pendek", "bobot": 4},
                    {"item": "Kaos santai", "bobot": 3},
                    {"item": "Sweater crew neck", "bobot": 2},
                    {"item": "Kemeja kasual", "bobot": 1}
                ],
                "bawahan": [
                    {"item": "Celana chino", "bobot": 4},
                    {"item": "Celana jeans", "bobot": 3},
                    {"item": "Celana jogger", "bobot": 2}
                ],
                "aksesori": [
                    {"item": "Jam tangan", "bobot": 3},
                    {"item": "Tas selempang", "bobot": 2},
                    {"item": "Kacamata hitam", "bobot": 1},
                    {"item": "Sepatu loafers", "bobot": 2}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Sweater tipis", "bobot": 4},
                    {"item": "Kaos santai", "bobot": 3},
                    {"item": "Blouse kasual", "bobot": 2},
                    {"item": "Kemeja oversized", "bobot": 1}
                ],
                "bawahan": [
                    {"item": "Celana jeans skinny", "bobot": 4},
                    {"item": "Celana kulot", "bobot": 3},
                    {"item": "Rok denim", "bobot": 2}
                ],
                "aksesori": [
                    {"item": "Tas selempang", "bobot": 3},
                    {"item": "Kacamata hitam", "bobot": 2},
                    {"item": "Jam tangan", "bobot": 1},
                    {"item": "Sepatu kets", "bobot": 2}
                ]
            }
        },
        "aturan": {
            "pria": [
                {
                    "nama": "Kasual Rapi",
                    "kombinasi": ["Kemeja lengan pendek", "Celana chino", "Sepatu loafers", "Jam tangan"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Gaya santai namun rapi untuk nongkrong di cafe."
                },
                {
                    "nama": "Kasual Stylish",
                    "kombinasi": ["Kaos santai", "Celana jeans", "Tas selempang", "Kacamata hitam"],
                    "bobot_min": 8,
                    "confidence_base": 80,
                    "deskripsi": "Tampilan kasual dengan sentuhan gaya untuk suasana cafe."
                }
            ],
            "wanita": [
                {
                    "nama": "Kasual Chic",
                    "kombinasi": ["Sweater tipis", "Celana jeans skinny", "Sepatu kets", "Tas selempang"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Gaya santai namun chic untuk ke cafe."
                },
                {
                    "nama": "Kasual Praktis",
                    "kombinasi": ["Blouse kasual", "Celana kulot", "Jam tangan", "Kacamata hitam"],
                    "bobot_min": 8,
                    "confidence_base": 80,
                    "deskripsi": "Kombinasi nyaman untuk bersantai di cafe."
                }
            ]
        }
    },
    "perpustakaan": {
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kemeja flanel", "bobot": 4},
                    {"item": "Kaos polos", "bobot": 3},
                    {"item": "Cardigan ringan", "bobot": 2},
                    {"item": "Sweater crew neck", "bobot": 1}
                ],
                "bawahan": [
                    {"item": "Celana chino", "bobot": 4},
                    {"item": "Celana jogger", "bobot": 3},
                    {"item": "Celana jeans", "bobot": 2}
                ],
                "aksesori": [
                    {"item": "Tote bag", "bobot": 3},
                    {"item": "Kacamata baca", "bobot": 2},
                    {"item": "Syal ringan", "bobot": 1},
                    {"item": "Sepatu kets", "bobot": 2}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Cardigan panjang", "bobot": 4},
                    {"item": "Kaos polos", "bobot": 3},
                    {"item": "Blouse santai", "bobot": 2},
                    {"item": "Sweater tipis", "bobot": 1}
                ],
                "bawahan": [
                    {"item": "Celana jeans", "bobot": 4},
                    {"item": "Celana kulot", "bobot": 3},
                    {"item": "Rok denim", "bobot": 2}
                ],
                "aksesori": [
                    {"item": "Tote bag", "bobot": 3},
                    {"item": "Kacamata baca", "bobot": 2},
                    {"item": "Syal ringan", "bobot": 1},
                    {"item": "Sepatu flat", "bobot": 2}
                ]
            }
        },
        "aturan": {
            "pria": [
                {
                    "nama": "Kasual Santai",
                    "kombinasi": ["Kemeja flanel", "Celana jeans", "Sepatu kets", "Tote bag"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Gaya santai untuk belajar di perpustakaan."
                },
                {
                    "nama": "Kasual Rapi",
                    "kombinasi": ["Cardigan ringan", "Celana formal", "Kacamata baca", "Syal ringan"],
                    "bobot_min": 8,
                    "confidence_base": 80,
                    "deskripsi": "Tampilan kasual yang cocok untuk suasana tenang."
                }
            ],
            "wanita": [
                {
                    "nama": "Kasual Feminin",
                    "kombinasi": ["Cardigan panjang", "Celana jeans", "Sepatu flat", "Tote bag"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Gaya santai dengan sentuhan feminin untuk perpustakaan."
                },
                {
                    "nama": "Kasual Nyaman",
                    "kombinasi": ["Kaos polos", "Celana kulot", "Syal ringan", "Kacamata baca"],
                    "bobot_min": 8,
                    "confidence_base": 80,
                    "deskripsi": "Kombinasi nyaman untuk belajar atau membaca."
                }
            ]
        }
    },
    "hiking": {
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Jaket outdoor", "bobot": 5},
                    {"item": "Kaos quick-dry", "bobot": 4},
                    {"item": "Kaos teknis", "bobot": 3},
                    {"item": "Hoodie tahan air", "bobot": 2}
                ],
                "bawahan": [
                    {"item": "Celana trekking", "bobot": 5},
                    {"item": "Celana cargo", "bobot": 4},
                    {"item": "Celana pendek hiking", "bobot": 3}
                ],
                "aksesori": [
                    {"item": "Topi rimba", "bobot": 3},
                    {"item": "Ransel hiking", "bobot": 2},
                    {"item": "Tongkat hiking", "bobot": 1},
                    {"item": "Sepatu hiking", "bobot": 2}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Jaket softshell", "bobot": 5},
                    {"item": "Kaos teknis", "bobot": 4},
                    {"item": "Tank top olahraga", "bobot": 3},
                    {"item": "Hoodie outdoor", "bobot": 2}
                ],
                "bawahan": [
                    {"item": "Legging hiking", "bobot": 4},
                    {"item": "Celana trekking", "bobot": 3},
                    {"item": "Celana pendek hiking", "bobot": 2}
                ],
                "aksesori": [
                    {"item": "Topi visor", "bobot": 3},
                    {"item": "Ransel hiking", "bobot": 2},
                    {"item": "Tongkat hiking", "bobot": 1},
                    {"item": "Sepatu hiking", "bobot": 2}
                ]
            }
        },
        "aturan": {
            "pria": [
                {
                    "nama": "Outdoor Fungsional",
                    "kombinasi": ["Jaket outdoor", "Celana trekking", "Sepatu hiking", "Topi rimba"],
                    "bobot_min": 12,
                    "confidence_base": 90,
                    "deskripsi": "Gaya fungsional untuk aktivitas hiking."
                },
                {
                    "nama": "Outdoor Praktis",
                    "kombinasi": ["Kaos quick-dry", "Celana cargo", "Ransel hiking", "Tongkat hiking"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Kombinasi praktis untuk pendakian ringan."
                }
            ],
            "wanita": [
                {
                    "nama": "Outdoor Stylish",
                    "kombinasi": ["Jaket softshell", "Legging hiking", "Sepatu hiking", "Topi visor"],
                    "bobot_min": 12,
                    "confidence_base": 90,
                    "deskripsi": "Gaya stylish namun fungsional untuk hiking."
                },
                {
                    "nama": "Outdoor Nyaman",
                    "kombinasi": ["Kaos teknis", "Celana trekking", "Ransel hiking", "Tongkat hiking"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Kombinasi nyaman untuk aktivitas outdoor."
                }
            ]
        }
    },
    "piknik": {
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kaos santai", "bobot": 4},
                    {"item": "Kemeja linen", "bobot": 3},
                    {"item": "Tank top kasual", "bobot": 2},
                    {"item": "Kaos katun", "bobot": 1}
                ],
                "bawahan": [
                    {"item": "Celana pendek linen", "bobot": 4},
                    {"item": "Celana pendek denim", "bobot": 3},
                    {"item": "Celana pendek kasual", "bobot": 2}
                ],
                "aksesori": [
                    {"item": "Topi pet", "bobot": 3},
                    {"item": "Keranjang piknik", "bobot": 2},
                    {"item": "Kacamata hitam", "bobot": 1},
                    {"item": "Sandal outdoor", "bobot": 2}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Dress santai floral", "bobot": 5},
                    {"item": "Kaos santai", "bobot": 3},
                    {"item": "Blouse kasual", "bobot": 2},
                    {"item": "Tank top katun", "bobot": 1}
                ],
                "bawahan": [
                    {"item": "Rok pendek", "bobot": 4},
                    {"item": "Celana pendek kasual", "bobot": 3},
                    {"item": "Celana jeans", "bobot": 2}
                ],
                "aksesori": [
                    {"item": "Topi jerami", "bobot": 3},
                    {"item": "Keranjang piknik", "bobot": 2},
                    {"item": "Kacamata hitam", "bobot": 1},
                    {"item": "Sandal jepit", "bobot": 2}
                ]
            }
        },
        "aturan": {
            "pria": [
                {
                    "nama": "Piknik Santai",
                    "kombinasi": ["Kaos santai", "Celana pendek linen", "Sandal outdoor", "Topi pet"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Gaya santai untuk piknik di alam terbuka."
                },
                {
                    "nama": "Piknik Praktis",
                    "kombinasi": ["Kemeja linen", "Celana pendek denim", "Keranjang piknik", "Kacamata hitam"],
                    "bobot_min": 8,
                    "confidence_base": 80,
                    "deskripsi": "Kombinasi praktis untuk hari piknik."
                }
            ],
            "wanita": [
                {
                    "nama": "Piknik Feminin",
                    "kombinasi": ["Dress santai floral", "Sandal jepit", "Topi jerami", "Keranjang piknik"],
                    "bobot_min": 12,
                    "confidence_base": 85,
                    "deskripsi": "Gaya feminin untuk piknik yang menyenangkan."
                },
                {
                    "nama": "Piknik Nyaman",
                    "kombinasi": ["Kaos santai", "Rok pendek", "Kacamata hitam", "Sandal jepit"],
                    "bobot_min": 8,
                    "confidence_base": 80,
                    "deskripsi": "Kombinasi nyaman untuk bersantai saat piknik."
                }
            ]
        }
    },
    "acara keluarga": {
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Batik modern", "bobot": 5},
                    {"item": "Kemeja lengan panjang", "bobot": 4},
                    {"item": "Kemeja batik", "bobot": 3},
                    {"item": "Kemeja formal", "bobot": 2}
                ],
                "bawahan": [
                    {"item": "Celana bahan slim-fit", "bobot": 5},
                    {"item": "Celana chino", "bobot": 4},
                    {"item": "Celana formal", "bobot": 3}
                ],
                "aksesori": [
                    {"item": "Jam tangan", "bobot": 3},
                    {"item": "Ikat pinggang kulit", "bobot": 2},
                    {"item": "Kacamata formal", "bobot": 1},
                    {"item": "Sepatu loafers", "bobot": 2}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Kebaya modern", "bobot": 5},
                    {"item": "Blouse elegan", "bobot": 4},
                    {"item": "Atasan batik", "bobot": 3},
                    {"item": "Kemeja sutra", "bobot": 2}
                ],
                "bawahan": [
                    {"item": "Rok batik", "bobot": 5},
                    {"item": "Rok midi", "bobot": 4},
                    {"item": "Celana bahan", "bobot": 3}
                ],
                "aksesori": [
                    {"item": "Tas kecil", "bobot": 3},
                    {"item": "Anting minimalis", "bobot": 2},
                    {"item": "Jam tangan", "bobot": 1},
                    {"item": "Sandal hak rendah", "bobot": 2}
                ]
            }
        },
        "aturan": {
            "pria": [
                {
                    "nama": "Semi-Formal Tradisional",
                    "kombinasi": ["Batik modern", "Celana bahan slim-fit", "Sepatu loafers", "Jam tangan"],
                    "bobot_min": 12,
                    "confidence_base": 90,
                    "deskripsi": "Gaya tradisional modern untuk acara keluarga."
                },
                {
                    "nama": "Semi-Formal Rapi",
                    "kombinasi": ["Kemeja lengan panjang", "Celana chino", "Ikat pinggang kulit", "Kacamata formal"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Tampilan rapi untuk acara keluarga."
                }
            ],
            "wanita": [
                {
                    "nama": "Elegan Tradisional",
                    "kombinasi": ["Kebaya modern", "Rok batik", "Sandal hak rendah", "Tas kecil"],
                    "bobot_min": 12,
                    "confidence_base": 90,
                    "deskripsi": "Gaya elegan dengan sentuhan tradisional."
                },
                {
                    "nama": "Semi-Formal Chic",
                    "kombinasi": ["Blouse elegan", "Rok midi", "Anting minimalis", "Jam tangan"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Kombinasi modern untuk acara keluarga."
                }
            ]
        }
    },
    "gym": {
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Tank top olahraga", "bobot": 5},
                    {"item": "Kaos dry-fit", "bobot": 4},
                    {"item": "Kaos teknis", "bobot": 3},
                    {"item": "Hoodie olahraga", "bobot": 2}
                ],
                "bawahan": [
                    {"item": "Celana training", "bobot": 5},
                    {"item": "Celana pendek olahraga", "bobot": 4},
                    {"item": "Celana jogger olahraga", "bobot": 3}
                ],
                "aksesori": [
                    {"item": "Handuk kecil", "bobot": 3},
                    {"item": "Botol air", "bobot": 2},
                    {"item": "Sarung tangan gym", "bobot": 1},
                    {"item": "Sepatu gym", "bobot": 2}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Sports bra", "bobot": 5},
                    {"item": "Tank top olahraga", "bobot": 4},
                    {"item": "Kaos dry-fit", "bobot": 3},
                    {"item": "Hoodie olahraga", "bobot": 2}
                ],
                "bawahan": [
                    {"item": "Legging gym", "bobot": 5},
                    {"item": "Celana pendek olahraga", "bobot": 4},
                    {"item": "Celana jogger olahraga", "bobot": 3}
                ],
                "aksesori": [
                    {"item": "Ikat rambut", "bobot": 3},
                    {"item": "Botol air", "bobot": 2},
                    {"item": "Sarung tangan gym", "bobot": 1},
                    {"item": "Sepatu gym", "bobot": 2}
                ]
            }
        },
        "aturan": {
            "pria": [
                {
                    "nama": "Gym Fungsional",
                    "kombinasi": ["Tank top olahraga", "Celana training", "Sepatu gym", "Handuk kecil"],
                    "bobot_min": 12,
                    "confidence_base": 90,
                    "deskripsi": "Gaya fungsional untuk sesi gym."
                },
                {
                    "nama": "Gym Praktis",
                    "kombinasi": ["Kaos dry-fit", "Celana pendek olahraga", "Botol air", "Sarung tangan gym"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Kombinasi praktis untuk latihan gym."
                }
            ],
            "wanita": [
                {
                    "nama": "Gym Stylish",
                    "kombinasi": ["Sports bra", "Legging gym", "Sepatu gym", "Ikat rambut"],
                    "bobot_min": 12,
                    "confidence_base": 90,
                    "deskripsi": "Gaya stylish untuk latihan di gym."
                },
                {
                    "nama": "Gym Nyaman",
                    "kombinasi": ["Tank top olahraga", "Celana pendek olahraga", "Botol air", "Sarung tangan gym"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Kombinasi nyaman untuk sesi gym."
                }
            ]
        }
    },
    "meeting": {
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kemeja formal", "bobot": 5},
                    {"item": "Jas blazer", "bobot": 4},
                    {"item": "Kemeja lengan panjang", "bobot": 3},
                    {"item": "Vest formal", "bobot": 2}
                ],
                "bawahan": [
                    {"item": "Celana bahan tailored", "bobot": 5},
                    {"item": "Celana formal", "bobot": 4},
                    {"item": "Celana chino", "bobot": 3}
                ],
                "aksesori": [
                    {"item": "Tas kerja", "bobot": 3},
                    {"item": "Jam tangan", "bobot": 2},
                    {"item": "Kacamata formal", "bobot": 1},
                    {"item": "Sepatu kulit", "bobot": 2}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Blazer formal", "bobot": 5},
                    {"item": "Kemeja sutra", "bobot": 4},
                    {"item": "Blouse formal", "bobot": 3},
                    {"item": "Kemeja lengan panjang", "bobot": 2}
                ],
                "bawahan": [
                    {"item": "Celana bahan tailored", "bobot": 5},
                    {"item": "Rok pensil", "bobot": 4},
                    {"item": "Celana formal", "bobot": 3}
                ],
                "aksesori": [
                    {"item": "Tas kerja", "bobot": 3},
                    {"item": "Jam tangan", "bobot": 2},
                    {"item": "Kacamata formal", "bobot": 1},
                    {"item": "Sepatu hak rendah", "bobot": 2}
                ]
            }
        },
        "aturan": {
            "pria": [
                {
                    "nama": "Formal Profesional",
                    "kombinasi": ["Kemeja formal", "Celana bahan tailored", "Sepatu kulit", "Tas kerja"],
                    "bobot_min": 12,
                    "confidence_base": 90,
                    "deskripsi": "Gaya profesional untuk meeting penting."
                },
                {
                    "nama": "Formal Rapi",
                    "kombinasi": ["Jas blazer", "Celana formal", "Jam tangan", "Kacamata formal"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Tampilan rapi untuk suasana formal."
                }
            ],
            "wanita": [
                {
                    "nama": "Formal Elegan",
                    "kombinasi": ["Blazer formal", "Celana bahan tailored", "Sepatu hak rendah", "Tas kerja"],
                    "bobot_min": 12,
                    "confidence_base": 90,
                    "deskripsi": "Gaya elegan untuk meeting profesional."
                },
                {
                    "nama": "Formal Chic",
                    "kombinasi": ["Kemeja sutra", "Rok pensil", "Jam tangan", "Kacamata formal"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Kombinasi chic untuk suasana formal."
                }
            ]
        }
    },
    "olahraga": {
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kaos dry-fit", "bobot": 5},
                    {"item": "Tank top olahraga", "bobot": 4},
                    {"item": "Kaos teknis", "bobot": 3},
                    {"item": "Hoodie olahraga", "bobot": 2}
                ],
                "bawahan": [
                    {"item": "Celana training longgar", "bobot": 5},
                    {"item": "Celana pendek olahraga", "bobot": 4},
                    {"item": "Celana jogger olahraga", "bobot": 3}
                ],
                "aksesori": [
                    {"item": "Topi olahraga", "bobot": 3},
                    {"item": "Botol air", "bobot": 2},
                    {"item": "Smartwatch", "bobot": 1},
                    {"item": "Sepatu lari", "bobot": 2}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Tank top olahraga", "bobot": 5},
                    {"item": "Sports bra", "bobot": 4},
                    {"item": "Kaos dry-fit", "bobot": 3},
                    {"item": "Hoodie olahraga", "bobot": 2}
                ],
                "bawahan": [
                    {"item": "Legging training", "bobot": 5},
                    {"item": "Celana pendek olahraga", "bobot": 4},
                    {"item": "Celana jogger olahraga", "bobot": 3}
                ],
                "aksesori": [
                    {"item": "Ikat rambut", "bobot": 3},
                    {"item": "Botol air", "bobot": 2},
                    {"item": "Smartwatch", "bobot": 1},
                    {"item": "Sepatu lari", "bobot": 2}
                ]
            }
        },
        "aturan": {
            "pria": [
                {
                    "nama": "Olahraga Fungsional",
                    "kombinasi": ["Kaos dry-fit", "Celana training longgar", "Sepatu lari", "Topi olahraga"],
                    "bobot_min": 12,
                    "confidence_base": 90,
                    "deskripsi": "Gaya fungsional untuk aktivitas olahraga."
                },
                {
                    "nama": "Olahraga Praktis",
                    "kombinasi": ["Tank top olahraga", "Celana pendek olahraga", "Botol air", "Smartwatch"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Kombinasi praktis untuk latihan ringan."
                }
            ],
            "wanita": [
                {
                    "nama": "Olahraga Stylish",
                    "kombinasi": ["Tank top olahraga", "Legging training", "Sepatu lari", "Ikat rambut"],
                    "bobot_min": 12,
                    "confidence_base": 90,
                    "deskripsi": "Gaya stylish untuk sesi olahraga."
                },
                {
                    "nama": "Olahraga Nyaman",
                    "kombinasi": ["Sports bra", "Celana pendek olahraga", "Botol air", "Smartwatch"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Kombinasi nyaman untuk aktivitas olahraga."
                }
            ]
        }
    },
    "event musik": {
        "checklist": {
            "pria": {
                "atasan": [
                    {"item": "Kaos grafis oversized", "bobot": 4},
                    {"item": "Kaos band", "bobot": 3},
                    {"item": "Jaket utility", "bobot": 2},
                    {"item": "Hoodie oversized", "bobot": 1}
                ],
                "bawahan": [
                    {"item": "Celana cargo longgar", "bobot": 4},
                    {"item": "Celana jeans straight-fit", "bobot": 3},
                    {"item": "Celana jogger", "bobot": 2}
                ],
                "aksesori": [
                    {"item": "Gelang chain", "bobot": 2},
                    {"item": "Topi bucket", "bobot": 3},
                    {"item": "Crossbody bag", "bobot": 1},
                    {"item": "Sepatu sneakers chunky", "bobot": 2}
                ]
            },
            "wanita": {
                "atasan": [
                    {"item": "Crop top statement", "bobot": 4},
                    {"item": "Kaos grafis", "bobot": 3},
                    {"item": "Jaket denim oversized", "bobot": 2},
                    {"item": "Sweater crop", "bobot": 1}
                ],
                "bawahan": [
                    {"item": "Celana wide-leg trousers", "bobot": 4},
                    {"item": "Celana jeans high-waist", "bobot": 3},
                    {"item": "Rok cargo pendek", "bobot": 2}
                ],
                "aksesori": [
                    {"item": "Gelang chain", "bobot": 2},
                    {"item": "Topi bucket", "bobot": 3},
                    {"item": "Crossbody bag", "bobot": 1},
                    {"item": "Sepatu combat boots", "bobot": 2}
                ]
            }
        },
        "aturan": {
            "pria": [
                {
                    "nama": "Street Hype",
                    "kombinasi": ["Kaos grafis oversized", "Celana cargo longgar", "Sepatu sneakers chunky", "Topi bucket"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Gaya hype modern untuk suasana event musik."
                },
                {
                    "nama": "Urban Kasual",
                    "kombinasi": ["Jaket utility", "Celana jeans straight-fit", "Gelang chain", "Crossbody bag"],
                    "bobot_min": 8,
                    "confidence_base": 80,
                    "deskripsi": "Tampilan urban yang stylish untuk konser musik."
                }
            ],
            "wanita": [
                {
                    "nama": "Bold Chic",
                    "kombinasi": ["Crop top statement", "Celana wide-leg trousers", "Sepatu combat boots", "Topi bucket"],
                    "bobot_min": 10,
                    "confidence_base": 85,
                    "deskripsi": "Gaya bold dan chic untuk event musik."
                },
                {
                    "nama": "Edgy Praktis",
                    "kombinasi": ["Kaos grafis", "Rok cargo pendek", "Gelang chain", "Crossbody bag"],
                    "bobot_min": 8,
                    "confidence_base": 80,
                    "deskripsi": "Kombinasi edgy yang praktis untuk vibe konser."
                }
            ]
        }
    }
}

event_list = list(outfit_rekomendasi.keys())