# Codex CLI Configuration

## Overview

This repository implements the authentication layer for Codex CLI using
OpenID Connect (OIDC), PKCE, OAuth 2.0 Token Exchange, and OpenAI API key
generation.

## Features

- OAuth 2.0 Authorization Code Flow.
- PKCE (S256) authentication.
- Local callback server on localhost.
- Automatic browser login.
- API key token exchange.
- Refresh token persistence.
- ChatGPT Plus / Pro credit redemption.
- Secure credential storage.

## Stack

- TypeScript
- React (Ink CLI UI)
- Express
- Node.js
- OAuth / OIDC
- PKCE
- OpenAI Platform APIs

## Security Rules

- Never log secrets.
- Store credentials with `0600` permissions.
- Validate state before exchanging tokens.
- Validate JWT format before decoding.
- Refresh expired ID tokens automatically.

## Development Standards

- Strict TypeScript.
- Async/await only.
- Modular authentication utilities.
- Comprehensive error handling.
- Production-ready logging.

## Testing Checklist

- PKCE generation.
- Callback validation.
- Token exchange.
- Refresh token flow.
- Credit redemption.
- Auth file persistence.
