# TDS Data Analyst Agent

An AI-powered data analysis agent built for the Tools in Data Science (TDS) course. This application allows users to upload questions and datasets to receive intelligent analysis and insights.

## 🚀 Quick Deployment to Vercel

### Step 1: Upload to GitHub
1. Create a new repository on GitHub
2. Upload all these files to your repository
3. Commit and push to main branch

### Step 2: Deploy to Vercel
1. Go to [vercel.com](https://vercel.com)
2. Sign up/login with your GitHub account
3. Click "New Project"
4. Import your GitHub repository
5. Vercel will auto-detect it's a Next.js project
6. Click "Deploy"

### Step 3: Add Environment Variables
1. In your Vercel dashboard, go to Project Settings
2. Click on "Environment Variables"
3. Add: `OPENAI_API_KEY` with your OpenAI API key
4. Redeploy the project

### Step 4: Update promptfoo Configuration
1. After deployment, copy your Vercel URL (e.g., `https://your-app.vercel.app`)
2. Open `promptfooconfig.yaml`
3. Replace `YOUR_VERCEL_URL` with your actual Vercel URL
4. Save the file

## 🧪 Running promptfoo Evaluation

After deployment, test your agent:

```bash
# Install promptfoo
npm install -g promptfoo

# Run evaluation (after updating the URL in promptfooconfig.yaml)
promptfoo eval

# View results
promptfoo view
```

## 📝 How to Use the Agent

1. **Create a questions file**: Make a `.txt` file with questions (one per line)
   ```
   What patterns do you see in this dataset?
   How can I improve data quality?
   What statistical tests should I run?
   ```

2. **Prepare your dataset** (optional): Upload CSV, JSON, or Excel files

3. **Upload and analyze**: Use the web interface to get AI-powered insights

## 🔧 Features

- **File Upload Support**: Questions (.txt) and datasets (.csv, .json, .xlsx)
- **AI Analysis**: Powered by OpenAI GPT-3.5-turbo
- **promptfoo Compatible**: Ready for LLM evaluation and testing
- **Vercel Optimized**: Fast, serverless deployment
- **Responsive UI**: Works on desktop and mobile

## 🛠️ Local Development

If you want to run locally:

```bash
# Install dependencies
npm install

# Create environment file
cp .env.example .env.local
# Add your OPENAI_API_KEY

# Run development server
npm run dev

# Open http://localhost:3000
```

## 📊 API Endpoints

- `POST /api/analyze` - Main endpoint for file-based analysis
- `POST /api/simple` - Simple text-based queries (for promptfoo)

## 🤖 promptfoo Integration

This agent is pre-configured for promptfoo evaluation with:
- Comprehensive test cases for TDS concepts
- Error handling for robust evaluation
- Multiple response format support
- Timeout and latency monitoring

## 🔑 Getting OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new secret key
5. Copy and use in your environment variables

## 🚨 Important Notes

- Make sure to add your OpenAI API key to Vercel environment variables
- The app supports up to 10MB file uploads
- Responses are limited to 2500 tokens to control costs
- All uploaded files are automatically cleaned up after processing

## 📈 Evaluation Results

After running promptfoo evaluation, you'll see:
- Response quality metrics
- Latency measurements
- Success/failure rates
- Detailed test results

Perfect for TDS course requirements and AI agent evaluation!

## 🆘 Troubleshooting

**Common Issues:**
- **API Key Error**: Make sure OPENAI_API_KEY is set in Vercel environment variables
- **File Upload Issues**: Check file size (max 10MB) and format (.txt, .csv, .json)
- **promptfoo Errors**: Ensure your Vercel URL is correct in promptfooconfig.yaml
- **Deployment Fails**: Check Vercel build logs for errors

**Getting Help:**
- Check Vercel deployment logs
- Verify environment variables are set
- Test API endpoints manually
- Review promptfoo configuration syntax

Good luck with your TDS project! 🎉
