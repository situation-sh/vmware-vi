# PropertyFilterUpdate

The *PropertyFilterUpdate* data object type contains a list of updates to data visible through a specific filter.  Note that if a property changes through multiple filters, then a client receives an update for each filter. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**object_set** | [**List[ObjectUpdate]**](ObjectUpdate.md) | Set of changes to object properties in the filter.  | [optional] 
**missing_set** | [**List[MissingObject]**](MissingObject.md) | Objects that could not be found on the server, but were specified in a *PropertyFilterSpec.objectSet*.  This field will only be populated for objects that were determined to be missing since the data version passed to *PropertyCollector.CheckForUpdates*, *PropertyCollector.WaitForUpdates*, or *PropertyCollector.WaitForUpdatesEx* and will not contain objects that were missing prior to that data version.  | [optional] 

## Example

```python
from vmware_vi.models.property_filter_update import PropertyFilterUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyFilterUpdate from a JSON string
property_filter_update_instance = PropertyFilterUpdate.from_json(json)
# print the JSON string representation of the object
print PropertyFilterUpdate.to_json()

# convert the object into a dict
property_filter_update_dict = property_filter_update_instance.to_dict()
# create an instance of PropertyFilterUpdate from a dict
property_filter_update_form_dict = property_filter_update.from_dict(property_filter_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


