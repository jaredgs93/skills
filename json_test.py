import streamlit as st
skills_sujeto_01 = {
  "toma_de_decisiones": {
    "resultado": "Alto",
    "grado_del_resultado": 6.9,
    "concision": {
      "resultado": "Media",
      "grado_del_resultado": 0.7,
      "velocidad": {
        "resultado": "Media",
        "grado_del_resultado": 0.51,
        "rapidez_habla": {
          "resultado": "Baja",
          "grado_del_resultado": 0.63
        },
        "fluidez": {
          "resultado": "Alta",
          "grado_del_resultado": 0.7
        },
        "rapidez": {
          "resultado": "Alta",
          "grado_del_resultado": 0.68
        }
      },
      "firmeza": {
        "resultado": "Alta",
        "grado_del_resultado": 0.79,
        "organizacion": {
          "resultado": "Media",
          "grado_del_resultado": 0.71
        },
        "tono_de_voz": {
          "resultado": "Passionately",
          "grado_del_resultado": 1
        }
      }
    },
    "claridad": {
      "resultado": "Alta",
      "grado_del_resultado": 0.77,
      "ejemplos": {
        "resultado": "Medio",
        "grado_del_resultado": 0.56
      },
      "vaguedad": {
        "resultado": "Baja",
        "grado_del_resultado": 1
      },
      "muletillas": {
        "resultado": "Baja",
        "grado_del_resultado": 1
      }
    }
  },
  "negociacion": {
    "resultado": "Media",
    "grado_del_resultado": 5,
    "empatia": {
      "resultado": "Normal",
      "grado_del_resultado": 0.5,
      "sonrisa": {
        "resultado": "Escasa",
        "grado_del_resultado": 1
      },
      "mirada": {
        "resultado": "Centrada",
        "grado_del_resultado": 1
      }
    },
    "argumentacion": {
      "resultado": "Buena",
      "grado_del_resultado": 0.79,
      "expresion": {
        "resultado": "Buena",
        "grado_del_resultado": 0.75
      },
      "calidad_argumentacion": {
        "resultado": "Buena",
        "grado_del_resultado": 0.79,
        "vaguedad": {
          "resultado": "Baja",
          "grado_del_resultado": 1
        },
        "fluidez": {
          "resultado": "Alta",
          "grado_del_resultado": 0.7
        }
      }
    }
  },
  "control_del_estres": {
    "resultado": "Alto",
    "grado_del_resultado": 0.63,
    "lenguaje_no_verbal": {
      "resultado": "Bueno",
      "grado_del_resultado": 7.5
    },
    "comunicacion": {
      "resultado": "Media",
      "grado_del_resultado": 5,
      "muletillas": {
        "resultado": "Baja",
        "grado_del_resultado": 1
      },
      "constancia": {
        "resultado": "Alta",
        "grado_del_resultado": 0.98
      },
      "ruido": {
        "resultado": "Medio",
        "grado_del_resultado": 0.85
      }
    },
    "expresion": {
      "resultado": "Buena",
      "grado_del_resultado": 0.75
    }
  },
  "liderazgo": {
    "resultado": "Bueno",
    "grado_del_resultado": 6.7,
    "concision_liderazgo": {
      "resultado": "Media",
      "grado_del_resultado": 5.6,
      "velocidad": {
        "resultado": "Media",
        "grado_del_resultado": 0.51,
        "rapidez_habla": {
          "resultado": "Baja",
          "grado_del_resultado": 0.63
        },
        "fluidez": {
          "resultado": "Alta",
          "grado_del_resultado": 0.7
        },
        "rapidez": {
          "resultado": "Alta",
          "grado_del_resultado": 0.68
        }
      },
      "exactitud": {
        "resultado": "Media",
        "grado_del_resultado": 6.7,
        "originalidad": {
          "resultado": "Alta",
          "grado_del_resultado": 0.8
        },
        "claridad": {
          "resultado": "Alta",
          "grado_del_resultado": 0.77,
          "ejemplos": {
            "resultado": "Medio",
            "grado_del_resultado": 0.56
          },
          "vaguedad": {
            "resultado": "Baja",
            "grado_del_resultado": 1
          },
          "muletillas": {
            "resultado": "Baja",
            "grado_del_resultado": 1
          }
        }
      }
    },
    "seguridad_liderazgo": {
      "resultado": "Media",
      "grado_del_resultado": 5.4,
      "mirada": {
        "resultado": "Centrada",
        "grado_del_resultado": 1
      },
      "uniformidad_voz": {
        "resultado": "Alta",
        "grado_del_resultado": 1
      },
      "serenidad": {
        "resultado": "Baja",
        "grado_del_resultado": 0.88
      }
    },
    "argumentacion_liderazgo": {
      "resultado": "Buena",
      "grado_del_resultado": 7.9,
      "argumentacion": {
        "resultado": "Buena",
        "grado_del_resultado": 0.79,
        "expresion": {
          "resultado": "Buena",
          "grado_del_resultado": 0.75
        },
        "calidad_argumentacion": {
          "resultado": "Buena",
          "grado_del_resultado": 0.79,
          "vaguedad": {
            "resultado": "Baja",
            "grado_del_resultado": 1
          },
          "fluidez": {
            "resultado": "Alta",
            "grado_del_resultado": 0.7
          }
        }
      },
      "respeto": {
        "resultado": "Mucho",
        "grado_del_resultado": 1
      }
    }
  },
  "creatividad": {
    "resultado": "Alta",
    "grado_del_resultado": 8,
    "calidad_texto": {
      "resultado": "Alta",
      "grado_del_resultado": 1
    },
    "lenguaje_no_verbal": {
      "resultado": "Bueno",
      "grado_del_resultado": 7.5
    }
  },
  "autoestima": {
    "resultado": "Alta",
    "grado_del_resultado": 7,
    "seguridad_persona": {
      "resultado": "Alta",
      "grado_del_resultado": 7,
      "seguridad_expresion": {
        "resultado": "Alta",
        "grado_del_resultado": 7,
        "seguridad_texto": {
          "resultado": "Alta",
          "grado_del_resultado": 8,
          "adecuacion_tema": {
            "resultado": "Alta",
            "grado_del_resultado": 1
          },
          "vaguedad": {
            "resultado": "Baja",
            "grado_del_resultado": 1
          },
          "muletillas": {
            "resultado": "Baja",
            "grado_del_resultado": 1
          }
        },
        "seguridad_audio": {
          "resultado": "Media",
          "grado_del_resultado": 5.1,
          "rapidez_habla": {
            "resultado": "Baja",
            "grado_del_resultado": 0.63
          },
          "fluidez": {
            "resultado": "Alta",
            "grado_del_resultado": 0.7
          },
          "rapidez": {
            "resultado": "Alta",
            "grado_del_resultado": 0.68
          }
        }
      },
      "posicion_corporal": {
        "resultado": "Buena",
        "grado_del_resultado": 1,
        "mirada": {
          "resultado": "Centrada",
          "grado_del_resultado": 1
        },
        "movimientos": {
          "resultado": "Regular",
          "grado_del_resultado": 0.83
        }
      }
    },
    "expresion": {
      "resultado": "Buena",
      "grado_del_resultado": 0.75
    }
  }
}

st.json(skills_sujeto_01)