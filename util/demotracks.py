#

from . import trackinfo
gen_track_code = trackinfo.gen_track_code
import math

def all_IDs() -> str:
    track_pieces = {}
    for i in range(36):
        track_pieces[i] = [{"x":0,"y":0,"z":i,"r":0}]

    track_name = "EveryPieceID"

    return gen_track_code(track_name, track_pieces)


def gen_sphere(radius: float, num_points: int) -> list[dict[str, int]]:
    points = []
    phi = math.pi * (3. - math.sqrt(5.))  # Golden angle in radians

    for i in range(num_points):
        y = 1 - (i / float(num_points - 1)) * 2  # Range from -1 to 1
        radius_at_y = math.sqrt(1 - y * y) * radius

        theta = phi * i

        x = math.cos(theta) * radius_at_y
        z = math.sin(theta) * radius_at_y

        points.append({'x': int(x), 'y': int(y * radius), 'z': int(z)})

    return points


def remove_duplicates(points) -> list[dict[str, int | float]]:
    unique_points = set((point['x'], point['y'], point['z']) for point in points)
    return [{'x': x, 'y': y, 'z': z} for x, y, z in unique_points]


def sphere_track(radius: float) -> str:
    coords = remove_duplicates(gen_sphere(radius=radius, num_points=100000))

    coords = [{'x': i["x"], 'y': 3*(i["y"] + radius) + a, 'z': i["z"], 'r':0} for i in coords for a in range(1)]

    blockId = 30
    print(f"{len(coords)} blocks")

    trackData = {29:coords, 5:[{"x":0,"y":radius * 6 + 1,"z":0,"r":0}]}
    return gen_track_code("Sphere" + str(radius), trackData)


#print(sphere_track(50))


print(all_IDs())
#test