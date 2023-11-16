# HostNvmeOverRdmaParameters

This data object represents the transport specific parameters necessary to establish an NVME over RDMA connection.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address of the connection target.  ***Since:*** vSphere API 7.0  | 
**address_family** | **str** | Indicates the type of the address specified above.  If unset, it is assumed to be an IPv4 address. The set of possible values is described in *HostNvmeTransportParametersNvmeAddressFamily_enum*. Note that not all of the address families may be supported for establishing a connection over RDMA.  ***Since:*** vSphere API 7.0  | [optional] 
**port_number** | **int** | The port number of the RDMA target port.  When IPv4/IPv6 is used as address family above, the port number needs to be specified. If this field is unset, a default value of 4420 is assumed as per the IANA assignment: https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.host_nvme_over_rdma_parameters import HostNvmeOverRdmaParameters

# TODO update the JSON string below
json = "{}"
# create an instance of HostNvmeOverRdmaParameters from a JSON string
host_nvme_over_rdma_parameters_instance = HostNvmeOverRdmaParameters.from_json(json)
# print the JSON string representation of the object
print HostNvmeOverRdmaParameters.to_json()

# convert the object into a dict
host_nvme_over_rdma_parameters_dict = host_nvme_over_rdma_parameters_instance.to_dict()
# create an instance of HostNvmeOverRdmaParameters from a dict
host_nvme_over_rdma_parameters_form_dict = host_nvme_over_rdma_parameters.from_dict(host_nvme_over_rdma_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


