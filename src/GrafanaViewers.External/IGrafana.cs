using Refit;
using System.Threading.Tasks;

namespace GrafanaViewers.External
{
    public interface IGrafana
    {
        [Get("/api/dashboards/uid/{uid}")]
        Task<object> GetDashboards(string request);

        [Get("/api/datasources")] 
        Task<object> GetDatasources(string request);

        [Get("/api/search")]
        Task<object> GetSearch(string request);
    }
}
