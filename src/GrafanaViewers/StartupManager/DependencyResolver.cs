using System.Diagnostics;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.ResponseCompression;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.OpenApi.Models;
using GrafanaViewers.ErrorHandling.Middleware;
using GrafanaViewers.Services;

namespace GrafanaViewers.StartupManager
{
    public static class DependencyResolver
    {
        public static IServiceCollection AddDefaultServices(this IServiceCollection services)
        {
            services.AddSingleton<Process>();
            services.AddSingleton<ISearchService, ISearchService>();

            return services;
        }

        public static IServiceCollection AddMvcConfigurations(this IServiceCollection services)
        {
            services
            .AddMvc(options => options.EnableEndpointRouting = false)
            .AddJsonOptions(options => 
                {
                    options.JsonSerializerOptions.PropertyNameCaseInsensitive = JsonConfiguration.Get().PropertyNameCaseInsensitive;
                    options.JsonSerializerOptions.IgnoreNullValues = JsonConfiguration.Get().IgnoreNullValues;
                    options.JsonSerializerOptions.PropertyNamingPolicy = JsonConfiguration.Get().PropertyNamingPolicy;
                    options.JsonSerializerOptions.Encoder = JsonConfiguration.Get().Encoder;
                    options.JsonSerializerOptions.WriteIndented = JsonConfiguration.Get().WriteIndented;
                }
            );

            return services;
        }

        public static IServiceCollection AddSwaggerConfiguration(this IServiceCollection services)
        {
            services.AddSwaggerGen(c =>
            {
                c.SwaggerDoc("v1", new OpenApiInfo { Title = "GrafanaViewers", Version = "v1" });
            });
            
            return services;
        }

        public static IServiceCollection AddGzipConfiguration(this IServiceCollection services)
        {       
            services.Configure<GzipCompressionProviderOptions>(options => options.Level = System.IO.Compression.CompressionLevel.Fastest);
            services.AddResponseCompression(options => { options.Providers.Add<GzipCompressionProvider>(); });

            return services;
        }


        public static IApplicationBuilder UseApiErrorHandlerMiddleware(this IApplicationBuilder builder)
        {
            return builder.UseMiddleware<ApiErrorHanlder>();
        }
    }
}