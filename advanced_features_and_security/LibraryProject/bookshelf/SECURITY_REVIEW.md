# Security Review

## Measures Implemented
The Django application was configured with HTTPS-related security settings to improve transport security and reduce exposure to common web attacks.

### Implemented Settings
- `SECURE_SSL_REDIRECT = True` ensures all HTTP traffic is redirected to HTTPS.
- `SECURE_HSTS_SECONDS = 31536000` enforces HTTPS usage for one year.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True` applies HSTS to subdomains.
- `SECURE_HSTS_PRELOAD = True` allows the domain to be included in browser preload lists.
- `SESSION_COOKIE_SECURE = True` ensures session cookies are only sent over HTTPS.
- `CSRF_COOKIE_SECURE = True` ensures CSRF cookies are only sent over HTTPS.
- `X_FRAME_OPTIONS = "DENY"` protects against clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True` prevents MIME-sniffing.
- `SECURE_BROWSER_XSS_FILTER = True` enables browser XSS filtering.

## Security Benefit
These measures improve confidentiality, strengthen browser-side protection, and reduce the risk of insecure communication or browser-based attacks.

## Potential Areas for Improvement
Further improvements may include:
- using a strong Content Security Policy (CSP)
- enabling secure proxy SSL headers behind load balancers
- regular dependency updates
- stronger password policies
- multi-factor authentication