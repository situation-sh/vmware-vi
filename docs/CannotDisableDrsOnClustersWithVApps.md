# CannotDisableDrsOnClustersWithVApps

This fault is thrown when an attempt is made to disable DRS on a cluster, which contains a vApp.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cannot_disable_drs_on_clusters_with_v_apps import CannotDisableDrsOnClustersWithVApps

# TODO update the JSON string below
json = "{}"
# create an instance of CannotDisableDrsOnClustersWithVApps from a JSON string
cannot_disable_drs_on_clusters_with_v_apps_instance = CannotDisableDrsOnClustersWithVApps.from_json(json)
# print the JSON string representation of the object
print CannotDisableDrsOnClustersWithVApps.to_json()

# convert the object into a dict
cannot_disable_drs_on_clusters_with_v_apps_dict = cannot_disable_drs_on_clusters_with_v_apps_instance.to_dict()
# create an instance of CannotDisableDrsOnClustersWithVApps from a dict
cannot_disable_drs_on_clusters_with_v_apps_form_dict = cannot_disable_drs_on_clusters_with_v_apps.from_dict(cannot_disable_drs_on_clusters_with_v_apps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


