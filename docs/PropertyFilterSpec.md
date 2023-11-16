# PropertyFilterSpec

Specify the property data that is included in a filter.  A filter can specify part of a single managed object, or parts of multiple related managed objects in an inventory hierarchy - for example, to collect updates from all virtual machines in a given folder. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prop_set** | [**List[PropertySpec]**](PropertySpec.md) | Set of properties to include in the filter, specified for each object type.  | 
**object_set** | [**List[ObjectSpec]**](ObjectSpec.md) | Set of specifications that determine the objects to filter.  | 
**report_missing_objects_in_results** | **bool** | Control how to report missing objects during filter creation.  If false or unset and *PropertyFilterSpec.objectSet* refers to missing objects, filter creation will fail with a *ManagedObjectNotFound* fault.  If true and *PropertyFilterSpec.objectSet* refers to missing objects, filter creation will not fail and missing objects will be reported via filter results. This is the recommended setting when *PropertyFilterSpec.objectSet* refers to transient objects.  In an *UpdateSet* missing objects will appear in the *PropertyFilterUpdate.missingSet* field.  In a *RetrieveResult* missing objects will simply be omitted from the objects field.  For a call to *PropertyCollector.RetrieveProperties* missing objects will simply be omitted from the results.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.property_filter_spec import PropertyFilterSpec

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyFilterSpec from a JSON string
property_filter_spec_instance = PropertyFilterSpec.from_json(json)
# print the JSON string representation of the object
print PropertyFilterSpec.to_json()

# convert the object into a dict
property_filter_spec_dict = property_filter_spec_instance.to_dict()
# create an instance of PropertyFilterSpec from a dict
property_filter_spec_form_dict = property_filter_spec.from_dict(property_filter_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


