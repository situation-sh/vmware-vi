# ArrayOfNoHost

A boxed array of *NoHost*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NoHost]**](NoHost.md) |  | 

## Example

```python
from vmware_vi.models.array_of_no_host import ArrayOfNoHost

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNoHost from a JSON string
array_of_no_host_instance = ArrayOfNoHost.from_json(json)
# print the JSON string representation of the object
print ArrayOfNoHost.to_json()

# convert the object into a dict
array_of_no_host_dict = array_of_no_host_instance.to_dict()
# create an instance of ArrayOfNoHost from a dict
array_of_no_host_form_dict = array_of_no_host.from_dict(array_of_no_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


