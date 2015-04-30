http://code.google.com/p/django-moderaptor/

=Moderaptor=
Moderaptor provides simple moderation of content on community driven websites using Django.

----

==Features==
===Reporting widget===
Users can quickly report any violation or abuse, selecting one of the abuse reasons defined by you.

===Quick moderation widget===
Any object reported for moderation is possible to quickly moderate in-place. If you are a moderator, you see a quickmod form in the same place where the reporting form is.

===Offensive words blacklist===
Simple blacklist with a template filter you can use wherever you need.

===Bans===
Due to a lack of good concept for this feature, currently it's only listing bans and deactivating the selected user. It's not connected to the other features in any way.

===Admin panel===
Everything can be managed through the django-admin.

===i18n===
Currently English and Polish, if you generate your local version, please provide me with the .po and I'll commit it to the project.

===Email report notifications===
Under development, not yet implemented.

----

==Requirements==
Developped under 1.2.0, however, it should work under any 1.1+
Form submit uses Jquery form plugin (http://malsup.com/jquery/form/)

==Installation==
 * Checkout the code
 * Move templates directory to your template_dir
 * Move /css, /js and /images to your static media directories.
 * Add 'moderaptor' to INSTALLED_APPS
 * Run syncdb
 * Include jquery.form.js
 * Include moderaptor.js
 * Include moderaptor.css

==Configuration==
===settings.py===
If you want reporting to be available only for signed in users 
{{{
SIGNED_IN_ONLY = True
}}}

Create a group for moderators and set the id of this user group, add any user groups you want
{{{
MODERATORS_GROUPS_IDS = [3,5,]
}}}

----

==Usage==
===Models===
You need to register the models you want to be moderated, in a similar way to django-tagging
{{{
import moderaptor
try:
    moderaptor.register(BlogPost) #example model
except moderaptor.AlreadyRegistered:
    pass    
}}}

===Templates===

Assuming you want to add this feature to blog posts f.ex. you need to edit the template where the blog post is rendered (f.ex. post.html, or post_on_list.html). In this example your app would be 'blog' and the model would be BlogPost

Load the templatetag
{{{
{% load mod_report %}
}}}

Put the following in the place where the 'report' icon should appear. 
{{{
{% report request 'blog' 'blogpost' post.id %}
}}}

In order to make the moderation work (hiding objects), you have to wrap your content (in this example, your post object) with proper conditionals:
{{{
{% if post.mod_reported.hide_object %}
    <p class="info">Post has been hidden by the moderators for {{ post.mod_reported.type }}.</p>
{% else %}
    {% if post.mod_reported and not post.mod_reported.resolved %}
        <p class="info">Post has been reported for {{ post.mod_reported.type }}</p>
    {% endif %}
    {{ post.text }}
{% endif %}
}}}

You can use the offensive words blacklist on the content
{{{
{% load censored %}
{{ post.text|censored }}
}}}

----

==Customization==
Some basic css is in moderaptor.css and the js in moderaptor.js. 
I'm not a UI designer (surprise!), so if you come up with a better theme, or better, modify it to use jquery.ui.themes or something, feel free to contribute.


==Support==

Please file a ticket if you find any issues, feel free to submit patches or contribute any extensions.
I'd be happy to see projects where you used this app, and if you have any useful suggestions or code proposals, let me know: zalew7 at gmail.

