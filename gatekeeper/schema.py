# Gatekeeper - Open source access control
# Copyright (C) 2018-2019 Steven Mirabito
#
# This file is part of Gatekeeper.
#
# Gatekeeper is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Gatekeeper is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Gatekeeper.  If not, see <http://www.gnu.org/licenses/>.

import graphene
from gatekeeper.access_points.schema import Query as AccessPointQuery
from gatekeeper.access_points.schema import Mutation as AccessPointMutation
from gatekeeper.users.schema import Query as UserQuery
from gatekeeper.users.schema import Mutation as UserMutation
from gatekeeper.groups.schema import Query as GroupQuery
from gatekeeper.groups.schema import Mutation as GroupMutation
from gatekeeper.realms.schema import Query as RealmQuery
from gatekeeper.realms.schema import Mutation as RealmMutation
from gatekeeper.configuration.schema import Query as ConfigurationQuery
from gatekeeper.configuration.schema import Mutation as ConfigurationMutation
from gatekeeper.tags.schema import Query as TagQuery
from gatekeeper.tags.schema import Mutation as TagMutation


# This class combines all of the app-level Query objects
class Query(
    AccessPointQuery,
    UserQuery,
    GroupQuery,
    RealmQuery,
    ConfigurationQuery,
    TagQuery,
    graphene.ObjectType
):
    pass


# This class combines all of the app-level Mutation objects
class Mutation(
    AccessPointMutation,
    UserMutation,
    GroupMutation,
    RealmMutation,
    ConfigurationMutation,
    TagMutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
