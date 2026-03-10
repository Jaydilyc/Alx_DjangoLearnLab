# Django Blog – Authentication System

## Overview

The authentication system for the **Django Blog Application** provides secure user account management using Django’s built-in authentication framework. This system enables users to **register, log in, log out, and manage their profiles**.

By leveraging Django’s authentication tools, the application ensures secure password handling, session management, and protection against common web vulnerabilities such as **CSRF attacks**.

---

# Features Implemented

The authentication system includes the following features:

## 1. User Registration

New users can create an account using a registration form.

The registration form extends Django’s built-in **UserCreationForm** and includes:

- username  
- email  
- password  
- password confirmation  

After successful registration, users can log in to access their profile and other authenticated features.

---

## 2. User Login

The login system uses Django’s built-in **LoginView** to authenticate users.

Features include:

- secure password verification  
- session management  
- automatic redirection after login  

Users must provide their **username and password** to access their account.

---

## 3. User Logout

Authenticated users can log out using Django’s **LogoutView**.

Once logged out:

- the user session is terminated  
- access to protected pages is restricted  
- the user is redirected to the home page  

---

## 4. Profile Management

Authenticated users can view and update their profile information.

Users can:

- view their username  
- view their email  
- update username  
- update email address  

The profile page is protected using Django’s **`login_required` decorator** to ensure only authenticated users can access it.

---

# Authentication URLs

The following URL routes handle authentication functionality:

| URL | Description |
|-----|-------------|
| `/register/` | Register a new user account |
| `/login/` | Login to an existing account |
| `/logout/` | Logout from the application |
| `/profile/` | View and update user profile |

---

# Forms Used

Two forms were implemented for authentication.

## UserRegisterForm

Extends Django’s **UserCreationForm** to include an email field.

Fields included:

- username  
- email  
- password1  
- password2  

---

## UserUpdateForm

Used to update profile details.

Fields included:

- username  
- email  

---

# Security Features

The authentication system relies on Django’s secure authentication framework and includes the following protections.

## Password Hashing

Passwords are securely stored using Django’s built-in hashing algorithms.

## CSRF Protection

All forms include **CSRF tokens** to prevent Cross-Site Request Forgery attacks.

## Login Protection

The profile page is protected using **`login_required`** to prevent unauthorized access.

## Session Management

Django automatically manages user sessions for login and logout.

---

# How to Test the Authentication System

Follow these steps to test the authentication features.

## 1. Start the Development Server

Run the server:

```bash
python manage.py runserver


# Blog Post Management Features

The Django Blog application supports full CRUD functionality for blog posts using Django class-based views.

## Features
- View all blog posts
- View details of a single post
- Create new posts
- Edit existing posts
- Delete posts

## Permissions
- All users can view posts
- Only authenticated users can create posts
- Only the author of a post can edit or delete it

## Routes
- `/posts/` – list all posts
- `/posts/new/` – create a new post
- `/posts/<int:pk>/` – view a specific post
- `/posts/<int:pk>/edit/` – edit a post
- `/posts/<int:pk>/delete/` – delete a post


# Comment Functionality

The blog application includes a comment system that allows users to interact with posts.

## Features
- Users can view comments under each post
- Authenticated users can add comments
- Comment authors can edit their comments
- Comment authors can delete their comments

## Comment Fields
- `post`
- `author`
- `content`
- `created_at`
- `updated_at`

## Comment URLs
- `/post/<int:pk>/comment/new/`
- `/comment/<int:pk>/update/`
- `/comment/<int:pk>/delete/`

## Permissions
- All users can read comments
- Only logged-in users can add comments
- Only the comment author can edit or delete their own comment