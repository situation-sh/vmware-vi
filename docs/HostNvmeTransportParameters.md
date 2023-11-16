# HostNvmeTransportParameters

This data object represents the transport specific parameters necessary to establish an NVM Express over Fabrics connection.  For some further information, see: - \"NVM Express over Fabrics 1.0\", Section 1.5.7, \"Connection\"    ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_nvme_transport_parameters import HostNvmeTransportParameters

# TODO update the JSON string below
json = "{}"
# create an instance of HostNvmeTransportParameters from a JSON string
host_nvme_transport_parameters_instance = HostNvmeTransportParameters.from_json(json)
# print the JSON string representation of the object
print HostNvmeTransportParameters.to_json()

# convert the object into a dict
host_nvme_transport_parameters_dict = host_nvme_transport_parameters_instance.to_dict()
# create an instance of HostNvmeTransportParameters from a dict
host_nvme_transport_parameters_form_dict = host_nvme_transport_parameters.from_dict(host_nvme_transport_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


