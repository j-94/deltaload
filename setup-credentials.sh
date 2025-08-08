#!/bin/bash

echo "🔧 Credentials Setup for Bookmark ETL System"
echo "============================================="
echo ""

# Function to prompt for input with default
prompt_with_default() {
    local prompt="$1"
    local default="$2"
    local value
    
    if [ -n "$default" ]; then
        read -p "$prompt [$default]: " value
        echo "${value:-$default}"
    else
        read -p "$prompt: " value
        echo "$value"
    fi
}

# Check current status
echo "📊 Current Status:"
bun check-credentials.ts --test
echo ""

echo "🚀 Setup Process:"
echo "Choose which credentials to configure:"
echo ""
echo "1) Twitter/X Scraping (for Grok conversations)"
echo "2) Twitter API (for timeline fetching)"  
echo "3) OpenAI API (for AI enrichment)"
echo "4) Anthropic API (for Claude AI)"
echo "5) Show setup instructions only"
echo "6) Exit"
echo ""

read -p "Enter your choice (1-6): " choice

case $choice in
    1)
        echo ""
        echo "🐦 Twitter/X Scraping Setup"
        echo "─────────────────────────────"
        echo "You need to get cookies from your browser:"
        echo ""
        echo "1. Log in to X.com in your browser"
        echo "2. Open Developer Tools (F12)"
        echo "3. Go to Application/Storage → Cookies"
        echo "4. Find these cookie values:"
        echo ""
        
        CT0_CURRENT="${X_CT0}"
        AUTH_TOKEN_CURRENT="${X_AUTH_TOKEN}"
        KDT_CURRENT="${X_KDT}"
        
        CT0=$(prompt_with_default "Enter ct0 cookie value" "$CT0_CURRENT")
        AUTH_TOKEN=$(prompt_with_default "Enter auth_token cookie value" "$AUTH_TOKEN_CURRENT")
        KDT=$(prompt_with_default "Enter kdt cookie value (optional)" "$KDT_CURRENT")
        
        echo ""
        echo "Add these to your environment:"
        echo "export X_CT0='$CT0'"
        echo "export X_AUTH_TOKEN='$AUTH_TOKEN'"
        [ -n "$KDT" ] && echo "export X_KDT='$KDT'"
        echo ""
        echo "Save to ~/.bashrc or ~/.zshrc to persist across sessions"
        ;;
        
    2)
        echo ""
        echo "🔗 Twitter API Setup"
        echo "──────────────────────"
        echo "Get credentials from: https://developer.twitter.com/en/portal/dashboard"
        echo ""
        
        BEARER_TOKEN_CURRENT="${TWITTER_BEARER_TOKEN}"
        
        BEARER_TOKEN=$(prompt_with_default "Enter Bearer Token" "$BEARER_TOKEN_CURRENT")
        
        echo ""
        echo "Add this to your environment:"
        echo "export TWITTER_BEARER_TOKEN='$BEARER_TOKEN'"
        echo ""
        echo "Save to ~/.bashrc or ~/.zshrc to persist across sessions"
        ;;
        
    3)
        echo ""
        echo "🤖 OpenAI API Setup"
        echo "─────────────────────"
        echo "Get API key from: https://platform.openai.com/api-keys"
        echo ""
        
        OPENAI_KEY_CURRENT="${OPENAI_API_KEY}"
        
        OPENAI_KEY=$(prompt_with_default "Enter OpenAI API Key" "$OPENAI_KEY_CURRENT")
        
        echo ""
        echo "Add this to your environment:"
        echo "export OPENAI_API_KEY='$OPENAI_KEY'"
        echo ""
        echo "Save to ~/.bashrc or ~/.zshrc to persist across sessions"
        ;;
        
    4)
        echo ""
        echo "🧠 Anthropic API Setup"
        echo "────────────────────────"
        echo "Get API key from: https://console.anthropic.com/"
        echo ""
        
        ANTHROPIC_KEY_CURRENT="${ANTHROPIC_API_KEY}"
        
        ANTHROPIC_KEY=$(prompt_with_default "Enter Anthropic API Key" "$ANTHROPIC_KEY_CURRENT")
        
        echo ""
        echo "Add this to your environment:"
        echo "export ANTHROPIC_API_KEY='$ANTHROPIC_KEY'"
        echo ""
        echo "Save to ~/.bashrc or ~/.zshrc to persist across sessions"
        ;;
        
    5)
        echo ""
        bun check-credentials.ts --setup
        ;;
        
    6)
        echo "Goodbye!"
        exit 0
        ;;
        
    *)
        echo "Invalid choice. Please run the script again."
        exit 1
        ;;
esac

echo ""
echo "✅ Setup complete!"
echo ""
echo "🔄 Test your configuration:"
echo "   bun check-credentials.ts --test"
echo ""
echo "🚀 Run the ETL pipeline:"
echo "   bun run-bookmark-etl-with-twitter.ts bookmarks.json"
echo ""
echo "📚 For more help:"
echo "   bun check-credentials.ts --help"