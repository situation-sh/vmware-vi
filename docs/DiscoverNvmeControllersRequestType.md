# DiscoverNvmeControllersRequestType

The parameters of *HostStorageSystem.DiscoverNvmeControllers*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discover_spec** | [**HostNvmeDiscoverSpec**](HostNvmeDiscoverSpec.md) |  | 

## Example

```python
from vmware_vi.models.discover_nvme_controllers_request_type import DiscoverNvmeControllersRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoverNvmeControllersRequestType from a JSON string
discover_nvme_controllers_request_type_instance = DiscoverNvmeControllersRequestType.from_json(json)
# print the JSON string representation of the object
print DiscoverNvmeControllersRequestType.to_json()

# convert the object into a dict
discover_nvme_controllers_request_type_dict = discover_nvme_controllers_request_type_instance.to_dict()
# create an instance of DiscoverNvmeControllersRequestType from a dict
discover_nvme_controllers_request_type_form_dict = discover_nvme_controllers_request_type.from_dict(discover_nvme_controllers_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


