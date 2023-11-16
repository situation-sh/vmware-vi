# ConnectNvmeControllerRequestType

The parameters of *HostStorageSystem.ConnectNvmeController*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connect_spec** | [**HostNvmeConnectSpec**](HostNvmeConnectSpec.md) |  | 

## Example

```python
from vmware_vi.models.connect_nvme_controller_request_type import ConnectNvmeControllerRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectNvmeControllerRequestType from a JSON string
connect_nvme_controller_request_type_instance = ConnectNvmeControllerRequestType.from_json(json)
# print the JSON string representation of the object
print ConnectNvmeControllerRequestType.to_json()

# convert the object into a dict
connect_nvme_controller_request_type_dict = connect_nvme_controller_request_type_instance.to_dict()
# create an instance of ConnectNvmeControllerRequestType from a dict
connect_nvme_controller_request_type_form_dict = connect_nvme_controller_request_type.from_dict(connect_nvme_controller_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


