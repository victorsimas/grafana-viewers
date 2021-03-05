using System.Threading.Tasks;
using GrafanaViewers.Requests;

namespace GrafanaViewers.Services
{
    public interface ISearchService
    {
        Task<dynamic> Get(SearchRequest request, string operation);
    }
}