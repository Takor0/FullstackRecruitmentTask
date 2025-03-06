import UserManager, {User} from "./user-manager";

const assertError = (fn: () => void) => {
    try {
        fn();
        console.assert(false);
    } catch (e) {
        console.assert(true);
    }
}

const userA: User = {
    id: 1,
    name: "test",
    email: "test@email.com",
    role: 'viewer',
    active: true,
    lastLogin: new Date("2021-01-01")
}
const userB: User = {
    id: 2,
    name: "test2",
    email: "test2@email.com",
    role: 'viewer',
    active: true,
    lastLogin: new Date("2021-05-01")
}

const TEST_USER_C_EMAIL = "test3@email.com"

const userC: User = {
    name: "test3",
    email: TEST_USER_C_EMAIL,
    role: 'admin',
    active: false,
    lastLogin: new Date("2021-03-01")
}

const userManager = new UserManager([userA, userB])

// Test addUser
const user = userManager.addUser(userC)
console.assert(user.id === 3)
console.assert(user.email === TEST_USER_C_EMAIL)
console.assert(userManager.searchUsers(TEST_USER_C_EMAIL).length === 1)
console.assert(userManager.searchUsers("not_exist").length === 0)

// Test getUserStats/updateUser
userManager.updateUser(3, {active: true})
const stats = userManager.getUserStats()
console.assert(stats.totalUsers === 3)
console.assert(stats.activeUsers === 3)
console.assert(stats.roleDistribution.viewer === 2)
console.assert(stats.roleDistribution.admin === 1)
console.assert(stats.roleDistribution.editor === 0)
console.assert(stats.avgLastLogin.getMonth() == 2)

// Test deleteUser
userManager.deleteUser(3)
console.assert(userManager.searchUsers(TEST_USER_C_EMAIL).length === 0)
assertError(() => userManager.deleteUser(3))

// Test getUserById
console.assert(userManager.getUserById(1).id === 1)

