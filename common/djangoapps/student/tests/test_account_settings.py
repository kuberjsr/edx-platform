"""Unit tests for custom UserProfile properties."""

import ddt

from django.test import TestCase
from student.views import validate_social_link, format_social_link


@ddt.ddt
class UserAccountSettingsTest(TestCase):
    """Unit tests for setting Social Media Links."""

    def setUp(self):
        super(UserAccountSettingsTest, self).setUp()

    def validate_social_link(self, social_platform, link):
        """
        Helper method that returns True if the social link is valid, False if
        the inputted link fails validation and will throw an error.
        """
        try:
            validate_social_link(social_platform, link)
        except ValueError:
            return False
        return True

    @ddt.data(
        ('facebook', 'www.facebook.com/edX', 'https://www.facebook.com/edX', True),
        ('facebook', 'www.evilwebsite.com/123', '', False),
        ('twitter', 'https://www.twitter.com/edX/123s', 'https://www.twitter.com/edX', True),
        ('twitter', 'twitter.com/edX', 'https://www.twitter.com/edX', True),
        ('linkedin', 'www.linkedin.com/harryrein', 'https://www.linkedin.com/harryrein', True),
        ('linkedin', 'www.evilwebsite.com/123?www.linkedin.com/edX', '', False),
        ('linkedin', '', '', True),
    )
    @ddt.unpack
    def test_social_link_input(self, platform, link, formatted_link, should_save):
        """
        Verify that social links are correctly validated and formatted.
        """
        # Ensure that invalid inputs fail validation
        validated_link = self.validate_social_link(platform, link)
        self.assertEquals(validated_link, should_save)

        # If input passes validation, ensure formatting works
        if validated_link:
            self.assertEquals(formatted_link, format_social_link(platform, link))
