# Use an official Node runtime as a parent image
FROM node:14

# Set environment variables
ENV NODE_ENV=production

# Create and set the working directory
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install app dependencies
RUN npm install --production

# Copy the app files to the working directory
COPY . .

# Expose port 3000 to the outside world
EXPOSE 3000

# Define the command to run on container start
CMD ["npm", "start"]
