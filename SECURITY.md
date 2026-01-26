# Security Policy

## 🔒 Protecting Your Secrets

This repository is designed to be safe for public sharing. However, when using this code, you must take precautions to protect your API keys and credentials.

## ✅ What's Already Protected

- ✅ The `.env` file is listed in `.gitignore` and will not be committed
- ✅ No secrets are hardcoded in the source code
- ✅ All credentials are loaded from environment variables
- ✅ The code fails safely if required environment variables are missing

## 🛡️ Security Best Practices

### 1. Never Commit Secrets

**DO NOT** commit files containing:
- API keys (Azure OpenAI, OpenAI, etc.)
- Access tokens
- Passwords
- Private keys
- Any other sensitive credentials

### 2. Use Environment Variables

This project uses a `.env` file for local development:

```bash
# Copy the example file
cp .env.example .env

# Edit .env with your actual credentials
# This file is automatically ignored by git
```

### 3. For Production Deployments

When deploying to production:
- Use secure secret management services (Azure Key Vault, AWS Secrets Manager, etc.)
- Use environment variables provided by your hosting platform
- Never store secrets in code or configuration files

### 4. Check Before Committing

Before committing code, always:
```bash
# Check what files will be committed
git status

# Review changes
git diff

# Make sure .env is not included
git ls-files | grep .env
# (Should only show .env.example, never .env)
```

### 5. If You Accidentally Commit a Secret

If you accidentally commit a secret:
1. **Immediately revoke/rotate the compromised credential**
2. Generate a new key/token
3. Consider the old key fully compromised (even if you remove it from git)
4. Update your `.env` with the new credential

⚠️ **Important**: Simply removing a secret from git history is NOT enough—secrets in git history can still be recovered. Always revoke compromised credentials.

## 🐛 Reporting Security Issues

If you discover a security vulnerability in this project, please:
1. **DO NOT** open a public GitHub issue
2. Email the maintainer privately with details
3. Allow time for the issue to be addressed before public disclosure

## 📚 Additional Resources

- [GitHub: Removing sensitive data from a repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
- [OWASP: Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [Azure: Best practices for securing Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/managed-identity)

## ✨ Summary

This repository is safe to share publicly as long as:
- You use the `.env` file for local credentials (never commit it)
- You don't hardcode any secrets in the code
- You follow the security best practices above

Happy coding! 🚀
