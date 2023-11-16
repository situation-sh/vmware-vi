# PropertySpec

Within a *PropertyFilterSpec*, A *PropertySpec* specifies which properties should be reported to the client for objects of the given managed object type that are visited and not skipped.  One more subtle side effect is that if a managed object is visited and not skipped, but there is no *PropertySpec* associated with the managed object's type, the managed object will not be reported to the client.  Also, the set of properties applicable to a given managed object type is the union of the properties implied by the *PropertySpec* objects even, in the case of a *RetrieveResult*, where there may be an applicable *PropertySpec* in more than one filter. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Name of the managed object type being collected.  | 
**all** | **bool** | Specifies whether or not all properties of the object are read.  If this property is set to true, the *PropertySpec.pathSet* property is ignored.  | [optional] 
**path_set** | **List[str]** | Specifies which managed object properties are retrieved.  If the *PropertySpec.pathSet* is empty, then the *PropertyCollector* retrieves references to the managed objects and no managed object properties are collected.  | [optional] 

## Example

```python
from vmware_vi.models.property_spec import PropertySpec

# TODO update the JSON string below
json = "{}"
# create an instance of PropertySpec from a JSON string
property_spec_instance = PropertySpec.from_json(json)
# print the JSON string representation of the object
print PropertySpec.to_json()

# convert the object into a dict
property_spec_dict = property_spec_instance.to_dict()
# create an instance of PropertySpec from a dict
property_spec_form_dict = property_spec.from_dict(property_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


