1. List All Blog Posts

Purpose: Display a list of all published blog posts.
URL: /
View: PostListView
Template: post_list.html
Access: Open to all users (no authentication required).

2. View a Single Blog Post
   Purpose: Display the details of a single blog post.
   URL: /post/<int:pk>/
   View: PostDetailView
   Template: post_detail.html
   Access: Open to all users (no authentication required).
   Details:

3. Create a New Blog Post
   Purpose: Allow authenticated users to create a new blog post.
   URL: /post/new/
   View: PostCreateView
   Template: post_form.html
   Access: Restricted to authenticated users.

4. Edit a Blog Post
   Purpose: Allow authors to update their blog posts.
   URL: /post/<int:pk>/edit/
   View: PostUpdateView
   Template: post_form.html
   Access: Restricted to the author of the post.
   Only the author of a post can edit it.
   Validation ensures the updated title and content fields are filled out.

5. Delete a Blog Post
   Purpose: Allow authors to delete their blog posts.
   URL: /post/<int:pk>/delete/
   View: PostDeleteView
   Template: post_confirm_delete.html
   Access: Restricted to the author of the post

Only the author of a post can delete it.
Confirmation is required before deletion

Authenticated Access:
Creating, editing, and deleting posts is restricted to logged-in users.
LoginRequiredMixin ensures unauthenticated users are redirected to the login page when attempting these actions.
Author-only Access:
Editing and deleting posts is restricted to the author of the post.
UserPassesTestMixin checks if the logged-in user is the author of the post.
