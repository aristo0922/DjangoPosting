# Generated by Django 4.2.2 on 2023-06-29 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("setdata", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ColumnsPriv",
        ),
        migrations.DeleteModel(
            name="Component",
        ),
        migrations.DeleteModel(
            name="Db",
        ),
        migrations.DeleteModel(
            name="DefaultRoles",
        ),
        migrations.DeleteModel(
            name="EngineCost",
        ),
        migrations.DeleteModel(
            name="Func",
        ),
        migrations.DeleteModel(
            name="GeneralLog",
        ),
        migrations.DeleteModel(
            name="GlobalGrants",
        ),
        migrations.DeleteModel(
            name="GtidExecuted",
        ),
        migrations.DeleteModel(
            name="HelpCategory",
        ),
        migrations.DeleteModel(
            name="HelpKeyword",
        ),
        migrations.DeleteModel(
            name="HelpRelation",
        ),
        migrations.DeleteModel(
            name="HelpTopic",
        ),
        migrations.DeleteModel(
            name="InnodbIndexStats",
        ),
        migrations.DeleteModel(
            name="InnodbTableStats",
        ),
        migrations.DeleteModel(
            name="PasswordHistory",
        ),
        migrations.DeleteModel(
            name="Plugin",
        ),
        migrations.DeleteModel(
            name="ProcsPriv",
        ),
        migrations.DeleteModel(
            name="ProxiesPriv",
        ),
        migrations.DeleteModel(
            name="ReplicationAsynchronousConnectionFailover",
        ),
        migrations.DeleteModel(
            name="ReplicationAsynchronousConnectionFailoverManaged",
        ),
        migrations.DeleteModel(
            name="ReplicationGroupConfigurationVersion",
        ),
        migrations.DeleteModel(
            name="ReplicationGroupMemberActions",
        ),
        migrations.DeleteModel(
            name="RoleEdges",
        ),
        migrations.DeleteModel(
            name="ServerCost",
        ),
        migrations.DeleteModel(
            name="Servers",
        ),
        migrations.DeleteModel(
            name="SlaveMasterInfo",
        ),
        migrations.DeleteModel(
            name="SlaveRelayLogInfo",
        ),
        migrations.DeleteModel(
            name="SlaveWorkerInfo",
        ),
        migrations.DeleteModel(
            name="SlowLog",
        ),
        migrations.DeleteModel(
            name="TablesPriv",
        ),
        migrations.DeleteModel(
            name="TimeZone",
        ),
        migrations.DeleteModel(
            name="TimeZoneLeapSecond",
        ),
        migrations.DeleteModel(
            name="TimeZoneName",
        ),
        migrations.DeleteModel(
            name="TimeZoneTransition",
        ),
        migrations.DeleteModel(
            name="TimeZoneTransitionType",
        ),
        migrations.DeleteModel(
            name="User",
        ),
        migrations.AlterModelTable(
            name="setdata",
            table="SETDATA",
        ),
    ]
