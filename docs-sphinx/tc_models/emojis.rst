############
Award Emojis
############

Reference
---------

* v4 API:

  + :class:`teamcity.v4.objects.ProjectIssueAwardEmoji`
  + :class:`teamcity.v4.objects.ProjectIssueNoteAwardEmoji`
  + :class:`teamcity.v4.objects.ProjectMergeRequestAwardEmoji`
  + :class:`teamcity.v4.objects.ProjectMergeRequestNoteAwardEmoji`
  + :class:`teamcity.v4.objects.ProjectSnippetAwardEmoji`
  + :class:`teamcity.v4.objects.ProjectSnippetNoteAwardEmoji`
  + :class:`teamcity.v4.objects.ProjectIssueAwardEmojiManager`
  + :class:`teamcity.v4.objects.ProjectIssueNoteAwardEmojiManager`
  + :class:`teamcity.v4.objects.ProjectMergeRequestAwardEmojiManager`
  + :class:`teamcity.v4.objects.ProjectMergeRequestNoteAwardEmojiManager`
  + :class:`teamcity.v4.objects.ProjectSnippetAwardEmojiManager`
  + :class:`teamcity.v4.objects.ProjectSnippetNoteAwardEmojiManager`


* GitLab API: https://docs.teamcity.com/ce/api/award_emoji.html

Examples
--------

List emojis for a resource::

   emojis = obj.awardemojis.list()

Get a single emoji::

   emoji = obj.awardemojis.get(emoji_id)

Add (create) an emoji::

   emoji = obj.awardemojis.create({'name': 'tractor'})

Delete an emoji::

   emoji.delete
   # or
   obj.awardemojis.delete(emoji_id)
