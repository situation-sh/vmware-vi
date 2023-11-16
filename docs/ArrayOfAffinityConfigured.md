# ArrayOfAffinityConfigured

A boxed array of *AffinityConfigured*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AffinityConfigured]**](AffinityConfigured.md) |  | 

## Example

```python
from vmware_vi.models.array_of_affinity_configured import ArrayOfAffinityConfigured

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAffinityConfigured from a JSON string
array_of_affinity_configured_instance = ArrayOfAffinityConfigured.from_json(json)
# print the JSON string representation of the object
print ArrayOfAffinityConfigured.to_json()

# convert the object into a dict
array_of_affinity_configured_dict = array_of_affinity_configured_instance.to_dict()
# create an instance of ArrayOfAffinityConfigured from a dict
array_of_affinity_configured_form_dict = array_of_affinity_configured.from_dict(array_of_affinity_configured_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


