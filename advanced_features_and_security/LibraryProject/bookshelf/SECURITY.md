# Security Measures Implemented

## 1. Secure Django Settings
The following security settings were added in `LibraryProject/settings.py`:

- `DEBUG = False`
- `SECURE_BROWSER_XSS_FILTER = True`
- `X_FRAME_OPTIONS = "DENY"`
- `SECURE_CONTENT_TYPE_NOSNIFF = True`
- `CSRF_COOKIE_SECURE = True`
- `SESSION_COOKIE_SECURE = True`

These settings improve browser-side protection and enforce secure cookies.

## 2. CSRF Protection
All form templates include `{% csrf_token %}` to protect against Cross-Site Request Forgery attacks.

## 3. Safe Data Handling
Views use Django forms and ORM instead of raw SQL queries.
This helps prevent SQL injection and validates user input safely.

## 4. Content Security Policy
A custom middleware was added to send the `Content-Security-Policy` header:

`default-src 'self'; script-src 'self'; style-src 'self'`

This reduces the risk of malicious script injection.

## 5. Template Safety
Django templates auto-escape variables by default, helping reduce XSS risk.