# Stage 1
FROM mcr.microsoft.com/dotnet/sdk:5.0.102-1-buster-slim-amd64 AS build
WORKDIR /build
COPY . .
RUN dotnet restore "src/GrafanaViewers/GrafanaViewers.csproj"
RUN dotnet publish "src/GrafanaViewers/GrafanaViewers.csproj" -c Release -o /app

# Stage 2
FROM mcr.microsoft.com/dotnet/aspnet:5.0.2-buster-slim-amd64 AS final
WORKDIR /app
COPY --from=build /app .
EXPOSE 5000
CMD dotnet GrafanaViewers.dll