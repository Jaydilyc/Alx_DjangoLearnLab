# HTTPS Deployment Configuration

## Django Security Settings
The following settings were added in `LibraryProject/settings.py` to enforce HTTPS and improve security:

- `SECURE_SSL_REDIRECT = True`
- `SECURE_HSTS_SECONDS = 31536000`
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`
- `SECURE_HSTS_PRELOAD = True`
- `SESSION_COOKIE_SECURE = True`
- `CSRF_COOKIE_SECURE = True`
- `X_FRAME_OPTIONS = "DENY"`
- `SECURE_CONTENT_TYPE_NOSNIFF = True`
- `SECURE_BROWSER_XSS_FILTER = True`

## Web Server HTTPS Configuration
In production, HTTPS must be enabled on the web server using an SSL/TLS certificate.

### Example with Nginx
- Install an SSL certificate
- Configure server blocks for HTTPS
- Redirect all HTTP traffic to HTTPS

Example approach:
1. Listen on port 80 and redirect requests to HTTPS
2. Listen on port 443 with SSL enabled
3. Provide certificate and private key paths

### Example Redirect Rule
All HTTP requests should be redirected to HTTPS to ensure encrypted communication.

## Notes
These settings help secure the Django application by:
- encrypting traffic
- protecting cookies
- preventing clickjacking
- reducing XSS risks
- enforcing browser HTTPS usage with HSTS