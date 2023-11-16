# HostNvmeOverTcpParameters

This data object represents the transport specific parameters necessary to establish an NVME over TCP connection.  ***Since:*** vSphere API 7.0.3.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address of the connection target.  It is expected to be an IPv4 or IPv6 address.  ***Since:*** vSphere API 7.0.3.0  | 
**port_number** | **int** | The port number of the TCP target port.  If this field is unset, the default value of 8009 is assumed as per the IANA assignment: https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**digest_verification** | **str** | Digest verification parameter.  When used in a discovery or connect spec, this parameter specifies the requested digest verification setting. The list of supported values is described in *HostDigestVerificationSetting_enum*. If unset, a default value of disabled is assumed. For details, see: - NVM Express Technical Proposal 8000 - NVMe/TCP Transport,   Section 7.4.10.2, \&quot;Initialize Connection Request PDU (ICReq)\&quot; - DGST field.    When part of *HostNvmeDiscoveryLogEntry*, this value is unset.  ***Since:*** vSphere API 7.0.3.0  | [optional] 

## Example

```python
from vmware_vi.models.host_nvme_over_tcp_parameters import HostNvmeOverTcpParameters

# TODO update the JSON string below
json = "{}"
# create an instance of HostNvmeOverTcpParameters from a JSON string
host_nvme_over_tcp_parameters_instance = HostNvmeOverTcpParameters.from_json(json)
# print the JSON string representation of the object
print HostNvmeOverTcpParameters.to_json()

# convert the object into a dict
host_nvme_over_tcp_parameters_dict = host_nvme_over_tcp_parameters_instance.to_dict()
# create an instance of HostNvmeOverTcpParameters from a dict
host_nvme_over_tcp_parameters_form_dict = host_nvme_over_tcp_parameters.from_dict(host_nvme_over_tcp_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


