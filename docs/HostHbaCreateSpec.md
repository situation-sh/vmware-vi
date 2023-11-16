# HostHbaCreateSpec

A data object which specifies the parameters needed to create a software host bus adapter of a specific kind.  ***Since:*** vSphere API 7.0.3.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_hba_create_spec import HostHbaCreateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostHbaCreateSpec from a JSON string
host_hba_create_spec_instance = HostHbaCreateSpec.from_json(json)
# print the JSON string representation of the object
print HostHbaCreateSpec.to_json()

# convert the object into a dict
host_hba_create_spec_dict = host_hba_create_spec_instance.to_dict()
# create an instance of HostHbaCreateSpec from a dict
host_hba_create_spec_form_dict = host_hba_create_spec.from_dict(host_hba_create_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


