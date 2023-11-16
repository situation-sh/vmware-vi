# ReadHostResourcePoolTreeFailed

Fault thrown on host connect if we were unable to correctly read the existing tree on the root.  This is bad because then we don't know the available resources on the host, and all kinds of admission control will fail. This just allows for more robust error handling - we should be able to read the existing hierarchy under normal conditions.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.read_host_resource_pool_tree_failed import ReadHostResourcePoolTreeFailed

# TODO update the JSON string below
json = "{}"
# create an instance of ReadHostResourcePoolTreeFailed from a JSON string
read_host_resource_pool_tree_failed_instance = ReadHostResourcePoolTreeFailed.from_json(json)
# print the JSON string representation of the object
print ReadHostResourcePoolTreeFailed.to_json()

# convert the object into a dict
read_host_resource_pool_tree_failed_dict = read_host_resource_pool_tree_failed_instance.to_dict()
# create an instance of ReadHostResourcePoolTreeFailed from a dict
read_host_resource_pool_tree_failed_form_dict = read_host_resource_pool_tree_failed.from_dict(read_host_resource_pool_tree_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


