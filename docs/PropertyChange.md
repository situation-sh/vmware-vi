# PropertyChange

Describes a change to a property. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Property or nested property to which the change applies.  Nested properties are specified by paths; for example, - foo.bar - foo.arProp\\[\&quot;key val\&quot;\\] - foo.arProp\\[\&quot;key val\&quot;\\].baz  | 
**op** | [**PropertyChangeOpEnum**](PropertyChangeOpEnum.md) |  | 
**val** | [**Any**](Any.md) |  | [optional] 

## Example

```python
from vmware_vi.models.property_change import PropertyChange

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyChange from a JSON string
property_change_instance = PropertyChange.from_json(json)
# print the JSON string representation of the object
print PropertyChange.to_json()

# convert the object into a dict
property_change_dict = property_change_instance.to_dict()
# create an instance of PropertyChange from a dict
property_change_form_dict = property_change.from_dict(property_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


