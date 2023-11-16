# DisconnectNvmeControllerRequestType

The parameters of *HostStorageSystem.DisconnectNvmeController*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disconnect_spec** | [**HostNvmeDisconnectSpec**](HostNvmeDisconnectSpec.md) |  | 

## Example

```python
from vmware_vi.models.disconnect_nvme_controller_request_type import DisconnectNvmeControllerRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DisconnectNvmeControllerRequestType from a JSON string
disconnect_nvme_controller_request_type_instance = DisconnectNvmeControllerRequestType.from_json(json)
# print the JSON string representation of the object
print DisconnectNvmeControllerRequestType.to_json()

# convert the object into a dict
disconnect_nvme_controller_request_type_dict = disconnect_nvme_controller_request_type_instance.to_dict()
# create an instance of DisconnectNvmeControllerRequestType from a dict
disconnect_nvme_controller_request_type_form_dict = disconnect_nvme_controller_request_type.from_dict(disconnect_nvme_controller_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


