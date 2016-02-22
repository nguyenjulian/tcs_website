from datetime import datetime

from django.core.management.base import BaseCommand

from apps.home.models import User
from apps.portfolio.models import Project, Tag, TagCategory


class Command(BaseCommand):

    def handle(self, **options):
        # === TagCategory =====================================================
        # Add TagCategories
        testing_tag_category = TagCategory(name='Testing')
        testing_tag_category.save()

        deployment_tag_category = TagCategory(name='Deployment')
        deployment_tag_category.save()

        production_tag_category = TagCategory(name='Production')
        production_tag_category.save()

        # === Tag =============================================================
        # Add prodution Tags
        java_tag = Tag(name='Java', category=production_tag_category)
        java_tag.save()

        python_tag = Tag(name='Python', category=production_tag_category)
        python_tag.save()

        cpp_tag = Tag(name='C++', category=production_tag_category)
        cpp_tag.save()

        csharp_tag = Tag(name='C#', category=production_tag_category)
        csharp_tag.save()

        dotnet_tag = Tag(name='dotnet', category=production_tag_category)
        dotnet_tag.save()

        # Add testing Tags
        junit_tag = Tag(name='junit', category=testing_tag_category)
        junit_tag.save()

        pythonunittest_tag = Tag(name='Python unittest', category=testing_tag_category)
        pythonunittest_tag.save()

        tox_tag = Tag(name='tox', category=testing_tag_category)
        tox_tag.save()

        selenium_tag = Tag(name='Selenium WebDriver', category=testing_tag_category)
        selenium_tag.save()

        jenkins_tag = Tag(name='Jenkins', category=testing_tag_category)
        jenkins_tag.save()

        virtualenv_tag = Tag(name="virtualenv", category=testing_tag_category)
        virtualenv_tag.save()

        # Add deployment Tags
        redhatopenshift_tag = Tag(name='RedHat Openshift', category=deployment_tag_category)
        redhatopenshift_tag.save()

        aws_tag = Tag(name='Amazon Web Services', category=deployment_tag_category)
        aws_tag.save()

        heroku_tag = Tag(name='Heroku', category=deployment_tag_category)
        heroku_tag.save()

        digitalocean_tag = Tag(name='Digital Ocean', category=deployment_tag_category)
        digitalocean_tag.save()

        # === User ============================================================
        brian_user = User(
            is_admin=True,
            is_client=False,
            first_name='Brian',
            last_name='Welch',
            member_since_date=datetime.today(),
            bio_description='Temporary bio.',
            linkedin_profile_url='https://linkedin.com/in/bwelch1',
            github_profile_url='https://github.com/welchbj')
        brian_user.save()

        julian_user = User(
            is_admin=False,
            is_client=False,
            first_name='Julian',
            last_name='Nguyen',
            member_since_date=datetime.today(),
            bio_description='Temporary bio.',
            linkedin_profile_url='https://linkedin.com/in/julian',
            github_profile_url='https://github.com/julian')
        julian_user.save()

        # === Project =========================================================
        tcswebsite_project = Project(
            name='TCS Website',
            short_description='The website that you are viewing right now.',
            github_url='https://www.github.com/fakeurl')
        tcswebsite_project.save()
        tcswebsite_project.developers.add(brian_user)
        tcswebsite_project.developers.add(julian_user)
        tcswebsite_project.tags.add(python_tag)
        tcswebsite_project.tags.add(selenium_tag)
        tcswebsite_project.tags.add(virtualenv_tag)
        tcswebsite_project.tags.add(redhatopenshift_tag)
        tcswebsite_project.save()

        samplebrian_project = Project(
            name='Sample Project by Brian',
            short_description='A cool project (by Brian).',
            github_url='https://www.github.com/fakeurl')
        samplebrian_project.save()
        samplebrian_project.developers.add(brian_user)
        samplebrian_project.tags.add(java_tag)
        samplebrian_project.tags.add(selenium_tag)
        samplebrian_project.tags.add(junit_tag)
        samplebrian_project.tags.add(aws_tag)
        samplebrian_project.tags.add(jenkins_tag)
        samplebrian_project.save()

        samplejulian_project = Project(
            name='Sample Project (by Julian)',
            short_description='An average project (by Julian)',
            github_url='https://www.github.com/fakeurl')
        samplejulian_project.save()
        samplejulian_project.developers.add(julian_user)
        samplejulian_project.tags.add(dotnet_tag)
        samplejulian_project.tags.add(cpp_tag)
        samplejulian_project.tags.add(selenium_tag)
        samplejulian_project.tags.add(heroku_tag)
        samplejulian_project.save()
