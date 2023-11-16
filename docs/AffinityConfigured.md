# AffinityConfigured

Virtual machine has a configured memory and/or CPU affinity that will prevent VMotion.  This is an error for powered-on virtual machines. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configured_affinity** | **List[str]** | Configured affinity types for the virtual machine.  See *AffinityType_enum* for valid values.  | 

## Example

```python
from vmware_vi.models.affinity_configured import AffinityConfigured

# TODO update the JSON string below
json = "{}"
# create an instance of AffinityConfigured from a JSON string
affinity_configured_instance = AffinityConfigured.from_json(json)
# print the JSON string representation of the object
print AffinityConfigured.to_json()

# convert the object into a dict
affinity_configured_dict = affinity_configured_instance.to_dict()
# create an instance of AffinityConfigured from a dict
affinity_configured_form_dict = affinity_configured.from_dict(affinity_configured_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


