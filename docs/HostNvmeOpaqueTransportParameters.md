# HostNvmeOpaqueTransportParameters

This data object represents the raw transport specific parameters returned in a Discovery Log Page Entry, when they cannot be interpreted as one of the known common types of parameters.  For details, see: - \"NVM Express over Fabrics 1.0\", Section 5.3,   Discovery Log Page    ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trtype** | **str** | The transport type.  Corresponds to the TRTYPE field in the Discovery Log Page Entry as specified by the NVME over Fabrics spec. The set of possible values is desribed in *HostNvmeTransportType_enum*.  ***Since:*** vSphere API 7.0  | 
**traddr** | **str** | The transport address.  Corresponds to the TRADDR field in the Discovery Log Page Entry as specified by the NVME over Fabrics spec.  ***Since:*** vSphere API 7.0  | 
**adrfam** | **str** | Indicates the address family of the address specified above.  Corresponds to the ADRFAM field in the Discovery Log Page Entry as specified by the NVME over Fabrics spec. The set of supported values is described in *HostNvmeTransportParametersNvmeAddressFamily_enum*.  ***Since:*** vSphere API 7.0  | 
**trsvcid** | **str** | Transport service identifier.  Corresponds to the TRSVCID field in the Discovery Log Page Entry as specified by the NVME over Fabrics spec. Its interpretation varies depending on the transport type.  ***Since:*** vSphere API 7.0  | 
**tsas** | **bytearray** | Transport specific address subtype.  Corresponds to the TSAS field in the Discovery Log Page Entry as specified by the NVME over Fabrics spec. Its interpretation varies depending on the transport type.  ***Since:*** vSphere API 7.0  | 

## Example

```python
from vmware_vi.models.host_nvme_opaque_transport_parameters import HostNvmeOpaqueTransportParameters

# TODO update the JSON string below
json = "{}"
# create an instance of HostNvmeOpaqueTransportParameters from a JSON string
host_nvme_opaque_transport_parameters_instance = HostNvmeOpaqueTransportParameters.from_json(json)
# print the JSON string representation of the object
print HostNvmeOpaqueTransportParameters.to_json()

# convert the object into a dict
host_nvme_opaque_transport_parameters_dict = host_nvme_opaque_transport_parameters_instance.to_dict()
# create an instance of HostNvmeOpaqueTransportParameters from a dict
host_nvme_opaque_transport_parameters_form_dict = host_nvme_opaque_transport_parameters.from_dict(host_nvme_opaque_transport_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


