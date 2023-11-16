# ArrayOfRelation

A boxed array of *Relation*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[Relation]**](Relation.md) |  | 

## Example

```python
from vmware_vi.models.array_of_relation import ArrayOfRelation

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfRelation from a JSON string
array_of_relation_instance = ArrayOfRelation.from_json(json)
# print the JSON string representation of the object
print ArrayOfRelation.to_json()

# convert the object into a dict
array_of_relation_dict = array_of_relation_instance.to_dict()
# create an instance of ArrayOfRelation from a dict
array_of_relation_form_dict = array_of_relation.from_dict(array_of_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


