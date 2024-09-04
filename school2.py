import numpy as np
from PIL import Image
from stl import mesh


def jpg_to_3d_stl(input_jpg, output_stl):

    # Загрузка изображения
    image = Image.open(input_jpg).convert('L')  # Конвертируем в grayscale
    print(image)
    width, height = image.size
    pixels = np.array(image)
    print()
    print()
    print()
    print(pixels)
    print()
    print()
    print()
    # Нормализация высоты
    max_height = 10.0  # Макс
    z_values = (pixels / 255.0) * max_height
    print(z_values)

    # Создание вершины и грани
    vertices = []
    faces = []
    kol = 0

    for y in range(height - 1):
        for x in range(width - 1):
            v1 = [x, y, z_values[y, x]]
            v2 = [x + 1, y, z_values[y, x + 1]]
            v3 = [x + 1, y + 1, z_values[y + 1, x + 1]]
            v4 = [x, y + 1, z_values[y + 1, x]]
            vertices.append(v1)
            vertices.append(v2)
            vertices.append(v3)
            vertices.append(v4)

            i = len(vertices)
            faces.append([i - 4, i - 3, i - 2])
            faces.append([i - 4, i - 2, i - 1])
            if kol == 0 or kol == 5 or kol == 2 or kol == 10:
                print(f'{kol} РАЗ --------  {faces}')
                print()
                print(z_values[y, x])
                print()
                print(f'{kol} РАЗ --------  {vertices}')
            kol += 1
    print()
    print()
    print()
    #print('faces', faces)
    print()
    print()
    print()
    #print('vertices', vertices)

    # Преобразование списки вершин и граней в numpy массивы
    vertices_2 = np.array(vertices)
    faces_2 = np.array(faces)

    # Создаение STL mesh
    surface = mesh.Mesh(np.zeros(faces_2.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces_2):
        for j in range(3):
            surface.vectors[i][j] = vertices_2[f[j], :]

    # Сохранение в STL файл
    surface.save(output_stl)


jpg_to_3d_stl('D:\Wing\pythonProject/venv/test1.jpg', 'output.stl')