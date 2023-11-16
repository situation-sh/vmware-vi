# ArrayOfHostNvmeController

A boxed array of *HostNvmeController*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNvmeController]**](HostNvmeController.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_nvme_controller import ArrayOfHostNvmeController

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNvmeController from a JSON string
array_of_host_nvme_controller_instance = ArrayOfHostNvmeController.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNvmeController.to_json()

# convert the object into a dict
array_of_host_nvme_controller_dict = array_of_host_nvme_controller_instance.to_dict()
# create an instance of ArrayOfHostNvmeController from a dict
array_of_host_nvme_controller_form_dict = array_of_host_nvme_controller.from_dict(array_of_host_nvme_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


