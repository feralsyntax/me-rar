from django.test import TestCase
from .models import Editor,Image,tag,Category,Location
import datetime as dt


# Create your tests here.
class EditorTestClass(TestCase):

    # set up method
    def setUp(self):
        self.benie = Editor(first_name='Benie',last_name='Langat',email='benie@gmail.com',phone='0712345678')

    # test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.benie,Editor))

    # test the save method
    def test_save_method(self):
        self.benie.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)


class tagTestClass(TestCase):

    # set up method
    def setUp(self):
        self.testertag = tag(name='testertag')

    # test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.testertag,tag))

    # test the save method
    def test_save_method(self):
        self.testertag.save_tag()
        tags = tag.objects.all()
        self.assertTrue(len(tags) > 0)


class CategoryTestClass(TestCase):

    # set up method
    def setUp(self):
        self.general = Category(category='general')

    # test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.general,Category))

    # test the save method
    def test_save_method(self):
        self.general.save_category()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys) > 0)

    def tearDown(self):
        Category.objects.filter(category='general').delete()

    def test_update_category(self):
        Category.objects.filter(category='general').update(category='health')


class LocationTestClass(TestCase):

    # set up method
    def setUp(self):
        self.mbagathi = Location(location='mbagathi')

    # test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.mbagathi,Location))

    # test the save method
    def test_save_method(self):
        self.mbagathi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def tearDown(self):
        Location.objects.filter(location='mbagathi').delete()

    def test_update_location(self):
        Location.objects.filter(location='mbagathi').update(location='Kisumu')


class ImageTestClass(TestCase):

    def setUp(self):
        # create a new editor & save
        self.benie = Editor(first_name='Benie',last_name='Langat',email='benie@gmail.com',phone='0712345678')
        self.benie.save_editor()

        # create a new tag & save it
        self.new_tag = tag(name='tester')
        self.new_tag.save()

        self.new_category = Category(category='general')
        self.new_category.save()

        self.new_location = Location(location='mbagathi')
        self.new_location.save()

        self.new_image = Image(pic='bg.jpg',title='Ozura',description='The landscape of heaven',editor=self.benie,category=self.new_category,location=self.new_location)
        self.new_image.save()

        self.new_image.tag.add(self.new_tag)


    def tearDown(self):
        Editor.objects.all().delete()
        tag.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_get_gallery_today(self):
        today_gallery = Image.todays_gallery()
        self.assertTrue(len(today_gallery) > 0)

    def test_get_gallery_by_date(self):
        test_date = '2022-05-26'
        date = dt.datetime.strptime(test_date,'%Y-%m-%d').date()
        gallery_by_date = Image.days_gallery(date)

        self.assertTrue(len(gallery_by_date) == 0)

    def test_search_by_tag(self):
        search_by_tag = Image.objects.filter(tag__name=self)

        return search_by_tag

    def test_search_by_category(self):
        search_by_category = Image.objects.filter(category__category=self)

        return search_by_category

    def test_search_by_location(self):
        search_by_location = Image.objects.filter(location__location=self)

        return search_by_location

    def test_get_by_id(self):
        get_by_id = Image.objects.filter(pic=self.id)

        return get_by_id

    def test_update_image(self):
        self.janja = Editor(first_name='Janja', last_name='Jay', email='jay@gmail.com', phone='0789675342')
        self.janja.save_editor()

        self.updated_tag = tag(name='newtag')
        self.updated_tag.save()

        self.updated_category = Category(category='health')
        self.updated_category.save()

        self.updated_location = Location(location='litein')
        self.updated_location.save()

        self.updated_image = Image.objects.filter(pic=self.id).update(pic='bg2.jpg',title='Alimbi',description='The truths of yesterday',editor=self.janja,category=self.updated_category,location=self.updated_location)
