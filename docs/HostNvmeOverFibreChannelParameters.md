# HostNvmeOverFibreChannelParameters

This data object represents the transport specific parameters necessary to establish an NVME over Fibre Channel connection.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_world_wide_name** | **int** | The world wide node name for the connection target.  ***Since:*** vSphere API 7.0  | 
**port_world_wide_name** | **int** | The world wide port name for the connection target.  ***Since:*** vSphere API 7.0  | 

## Example

```python
from vmware_vi.models.host_nvme_over_fibre_channel_parameters import HostNvmeOverFibreChannelParameters

# TODO update the JSON string below
json = "{}"
# create an instance of HostNvmeOverFibreChannelParameters from a JSON string
host_nvme_over_fibre_channel_parameters_instance = HostNvmeOverFibreChannelParameters.from_json(json)
# print the JSON string representation of the object
print HostNvmeOverFibreChannelParameters.to_json()

# convert the object into a dict
host_nvme_over_fibre_channel_parameters_dict = host_nvme_over_fibre_channel_parameters_instance.to_dict()
# create an instance of HostNvmeOverFibreChannelParameters from a dict
host_nvme_over_fibre_channel_parameters_form_dict = host_nvme_over_fibre_channel_parameters.from_dict(host_nvme_over_fibre_channel_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


