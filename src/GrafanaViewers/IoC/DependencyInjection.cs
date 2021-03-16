using System;
using GrafanaViewers.External;
using GrafanaViewers.Services;
using GrafanaViewers.StartupManager;
using Microsoft.Extensions.DependencyInjection;

namespace GrafanaViewers.IoC
{
    public static class DependencyInjection
    {
        public static IServiceCollection AddApiServices(this IServiceCollection services)
        {
            services.AddSingleton<ISearchService, SearchService>();

            return services;
        }

        public static IServiceCollection AddExternalServices(this IServiceCollection services)
        {
            services.RegisterRefitService<IGrafana>(Environment.GetEnvironmentVariable("HOST_GRAFANA"));

            return services;
        }
    }
}