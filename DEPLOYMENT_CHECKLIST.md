# 🚀 TDS Agent Deployment Checklist

## Pre-Deployment
- [ ] Have OpenAI API key ready
- [ ] GitHub account set up
- [ ] Vercel account created (free tier is fine)

## Upload to GitHub
- [ ] Create new GitHub repository
- [ ] Upload all project files
- [ ] Commit to main branch
- [ ] Repository is public or accessible to Vercel

## Deploy to Vercel
- [ ] Import GitHub repository to Vercel
- [ ] Vercel auto-detects as Next.js project
- [ ] Initial deployment completes successfully
- [ ] Copy your Vercel URL (e.g., https://your-app.vercel.app)

## Configure Environment
- [ ] Add OPENAI_API_KEY in Vercel dashboard
- [ ] Redeploy after adding environment variable
- [ ] Test the web interface works

## Update promptfoo Config
- [ ] Replace YOUR_VERCEL_URL in promptfooconfig.yaml
- [ ] Save the updated configuration

## Test Everything
- [ ] Web interface loads correctly
- [ ] File upload works
- [ ] Questions generate responses
- [ ] API endpoints respond correctly
- [ ] promptfoo evaluation runs without JSON errors

## Ready! 🎉
Your TDS Data Analyst Agent is deployed and working!

## URLs to Remember
- **Your App**: https://YOUR_VERCEL_URL.vercel.app
- **API Endpoint**: https://YOUR_VERCEL_URL.vercel.app/api/simple
- **GitHub Repo**: https://github.com/YOUR_USERNAME/YOUR_REPO_NAME
