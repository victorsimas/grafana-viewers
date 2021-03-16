using Refit;
using System.Threading.Tasks;

namespace GrafanaViewers.External
{
    public interface IGrafana
    {
        [Get("/maispontos/pedidos/calculopontos")]
        Task<dynamic> ObterTotalPontos(dynamic request);
    }
}
