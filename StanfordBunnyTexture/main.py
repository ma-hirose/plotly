import plotly.graph_objects as go
import numpy as np

# STLファイルの読み込み
def read_stl_file(file_path):
    with open(file_path, 'rb') as f:
        # ヘッダー情報を読み込み
        f.read(80)  # 80バイトのダミーヘッダーをスキップ

        # 三角形の面の数を読み込み
        num_faces = int.from_bytes(f.read(4), byteorder='little')

        vertices = []
        faces = []

        for _ in range(num_faces):
            # 法線ベクトルを読み込み（不要なのでスキップ）
            f.read(12)

            # 頂点座標を読み込み
            vertex1 = np.frombuffer(f.read(12), dtype=np.float32)
            vertex2 = np.frombuffer(f.read(12), dtype=np.float32)
            vertex3 = np.frombuffer(f.read(12), dtype=np.float32)

            # 頂点座標をリストに追加
            vertices.append(vertex1)
            vertices.append(vertex2)
            vertices.append(vertex3)

            # 面を構成する頂点のインデックスをリストに追加
            idx = len(vertices) - 3
            faces.append([idx, idx + 1, idx + 2])

            # フェイスの属性情報をスキップ
            f.read(2)

    return np.array(vertices), np.array(faces)

# STLファイルのパス
stl_file = 'stanford_bunny.stl'

# STLファイルの読み込み
vertices, faces = read_stl_file(stl_file)

# 初期の色設定
initial_color = 'lightpink'
initial_opacity = 1.0
initial_ambient = 0.5
initial_shadow_intensity = 0.5  # 影の初期値
initial_diffuse = 1
initial_roughness = 0.5
initial_specular = 0.2

# 3Dメッシュの作成
mesh = go.Mesh3d(
    x=vertices[:, 0],
    y=vertices[:, 1],
    z=vertices[:, 2],
    i=faces[:, 0],
    j=faces[:, 1],
    k=faces[:, 2],
    color=initial_color,
    opacity=initial_opacity,
    lighting=dict(ambient=initial_ambient,  # 影の濃さを調整
                  diffuse=initial_diffuse,  # 影の明るさを調整
                  roughness=initial_roughness,  # 影の粗さを調整
                  specular=initial_specular  # 光沢を調整
                  ),
)

# レイアウト設定
slider_start = (0, 0)
slider_diff = 0.01
slider_length = 0.18
pad_info = {"t": 10, "b":10, "r":10, "l":10}

colors_list = [
    'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure',
    'beige', 'bisque', 'black', 'blanchedalmond', 'blue',
    'blueviolet', 'brown', 'burlywood', 'cadetblue',
    'chartreuse', 'chocolate', 'coral', 'cornflowerblue',
    'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan',
    'darkgoldenrod', 'darkgray', 'darkgrey', 'darkgreen',
    'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange',
    'darkorchid', 'darkred', 'darksalmon', 'darkseagreen',
    'darkslateblue', 'darkslategray', 'darkslategrey',
    'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue',
    'dimgray', 'dimgrey', 'dodgerblue', 'firebrick',
    'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro',
    'ghostwhite', 'gold', 'goldenrod', 'gray', 'grey', 'green',
    'greenyellow', 'honeydew', 'hotpink', 'indianred', 'indigo',
    'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen',
    'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan',
    'lightgoldenrodyellow', 'lightgray', 'lightgrey',
    'lightgreen', 'lightpink', 'lightsalmon', 'lightseagreen',
    'lightskyblue', 'lightslategray', 'lightslategrey',
    'lightsteelblue', 'lightyellow', 'lime', 'limegreen',
    'linen', 'magenta', 'maroon', 'mediumaquamarine',
    'mediumblue', 'mediumorchid', 'mediumpurple',
    'mediumseagreen', 'mediumslateblue', 'mediumspringgreen',
    'mediumturquoise', 'mediumvioletred', 'midnightblue',
    'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy',
    'oldlace', 'olive', 'olivedrab', 'orange', 'orangered',
    'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise',
    'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink',
    'plum', 'powderblue', 'purple', 'red', 'rosybrown',
    'royalblue', 'saddlebrown', 'salmon', 'sandybrown',
    'seagreen', 'seashell', 'sienna', 'silver', 'skyblue',
    'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen',
    'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise',
    'violet', 'wheat', 'white', 'whitesmoke', 'yellow',
    'yellowgreen'
]

# Convert color names to a list of dictionaries
colors_dict_list = [
    dict(args=[{'color': color}], label=color, method='update')
    for color in colors_list
]

layout = go.Layout(
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
    ),
    margin=dict(l=0, r=0, t=0, b=0),
    updatemenus=[
        dict(
            # buttons=list([
            #     dict(
            #         args=[{'color': 'lightpink'}],
            #         label='Light Pink',
            #         method='update'
            #     ),
            #     dict(
            #         args=[{'color': 'lightblue'}],
            #         label='Light Blue',
            #         method='update'
            #     ),
            #     dict(
            #         args=[{'color': 'lightgreen'}],
            #         label='Light Green',
            #         method='update'
            #     ),
            #     dict(
            #         args=[{'color': 'gray'}],
            #         label='Light Green',
            #         method='update'
            #     )
            # ]),
            buttons=list(colors_dict_list),
            direction='up',
            pad={'r': 0, 't': 0},
            showactive=True,
            x=0.99,
            xanchor='right',
            y=-0.1,
            yanchor='bottom'
        ),
    ],
    sliders=[

        # 透明度
        dict(
            active=20,
            currentvalue={"prefix": "Opacity: "},
            pad=pad_info,
            steps=[
                dict(method="update", args=[{"opacity": i}], label=f"{i:.1f}")
                for i in np.arange(0, 1.05, 0.05)
            ],
            x=slider_start[0], 
            y=slider_start[0],
            len=slider_length,
            visible=True,  # スライダーを表示する
        ),
        
        # ライティングに関して
        dict(
            active=10,
            currentvalue={"prefix": "Ambient: "},
            pad=pad_info,
            steps=[
                dict(method="update", args=[{"lighting.ambient": i}], label=f"{i:.1f}")
                for i in np.arange(0, 1.05, 0.05)
            ],
            x=slider_start[0] + slider_length,
            y=slider_start[0],
            len=slider_length,
            visible=True,  # スライダーを表示する
        ),
        
        # ライティングに関して
        dict(
            active=20,
            currentvalue={"prefix": "Diffuse: "},
            pad=pad_info,
            steps=[
                dict(method="update", args=[{"lighting.diffuse": i}], label=f"{i:.1f}")
                for i in np.arange(0, 1.05, 0.05)
            ],
            x=slider_start[0] + slider_length*2, 
            y=slider_start[0],
            len=slider_length,
            visible=True,  # スライダーを表示する
        ),   
        
        dict(
            active=10,
            currentvalue={"prefix": "Roughness: "},
            pad=pad_info,
            steps=[
                dict(method="update", args=[{"lighting.roughness": i}], label=f"{i:.1f}")
                for i in np.arange(0, 1.05, 0.05)
            ],
            x=slider_start[0] + slider_length*3,
            y=slider_start[0],
            len=slider_length,
            visible=True,  # スライダーを表示する
        ),

        dict(
            active=4,
            currentvalue={"prefix": "Specular: "},
            pad=pad_info,
            steps=[
                dict(method="update", args=[{"lighting.specular": i}], label=f"{i:.1f}")
                for i in np.arange(0, 1.05, 0.05)
            ],
            x=slider_start[0] + slider_length*4, 
            y=slider_start[0],
            len=slider_length,
            visible=True,  # スライダーを表示する
        ),   
                
        
    ]
)

import plotly.offline as pyo

# プロット
fig = go.Figure(data=[mesh], layout=layout)
fig.update_traces()

# グラフの表示
fig.show()

pyo.plot(fig, filename='graph.html')
