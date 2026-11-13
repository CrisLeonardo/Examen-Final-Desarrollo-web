from rest_framework.test import APITestCase
from .models import Animal


class AnimalAPITests(APITestCase):
    def setUp(self):
        self.datos = {'nombre': 'Luna', 'especie': 'Perro', 'raza': 'Labrador', 'edad': 3}

    def test_guardar_y_obtener_registro(self):
        respuesta = self.client.post('/api/animales/', self.datos, format='json')
        self.assertEqual(respuesta.status_code, 201)
        animal = Animal.objects.get(pk=respuesta.data['id'])
        self.assertEqual(animal.nombre, 'Luna')
        self.assertIsNotNone(animal.created_at)
        self.assertIsNotNone(animal.updated_at)
        detalle = self.client.get(f'/api/animales/{animal.id}/')
        self.assertEqual(detalle.status_code, 200)
        self.assertEqual(detalle.data['raza'], 'Labrador')
        listado = self.client.get('/api/animales/')
        self.assertEqual(listado.status_code, 200)
        self.assertEqual(len(listado.data), 1)

    def test_rechaza_datos_incompletos_y_edad_negativa(self):
        self.assertEqual(self.client.post('/api/animales/', {}, format='json').status_code, 400)
        self.datos['edad'] = -1
        respuesta = self.client.post('/api/animales/', self.datos, format='json')
        self.assertEqual(respuesta.status_code, 400)
        self.assertIn('edad', respuesta.data)
        self.assertFalse(Animal.objects.exists())

    def test_editar_y_eliminar(self):
        animal = Animal.objects.create(**self.datos)
        url = f'/api/animales/{animal.id}/'
        anterior = animal.updated_at
        respuesta = self.client.patch(url, {'edad': 4}, format='json')
        self.assertEqual(respuesta.status_code, 200)
        animal.refresh_from_db()
        self.assertEqual(animal.edad, 4)
        self.assertGreater(animal.updated_at, anterior)
        datos = {**self.datos, 'nombre': 'Max'}
        self.assertEqual(self.client.put(url, datos, format='json').status_code, 200)
        self.assertEqual(self.client.delete(url).status_code, 204)
        self.assertFalse(Animal.objects.filter(pk=animal.id).exists())
        self.assertEqual(self.client.get(url).status_code, 404)
