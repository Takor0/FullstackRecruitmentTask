type UserRole = 'admin' | 'editor' | 'viewer';

export interface User {
    id?: number; // CHANGE: id should be optional if addUser handle user without provided id
    name: string;
    email: string;
    role: UserRole;
    active: boolean;
    lastLogin?: Date;
}

interface UserStats {
    totalUsers: number;
    activeUsers: number;
    roleDistribution: Record<UserRole, number>; // Number of users per role
    avgLastLogin?: Date | null; // Average last login date among users with last login  // CHANGE: Date | null
}

// User management class
export default class UserManager {
    private readonly users: User[] = [];

    constructor(initialUsers?: User[]) { // CHANGE:  Array<User> to User[]
        this.users = initialUsers;
    }


    // Add a new user
    public addUser(user: User): User { // CHANGE: Return the added user
        // Check if user with same email already exists
        const existing = this.users.find(u => u.email === user.email); // CHANGE: changed = to ===
        if (existing) {
            throw new Error(`User with email ${user.email} already exists`);
        }

        // Assign ID if not provided
        if (!user.id) {
            user.id = this.getNextId();
        }

        this.users.push(user);
        return user; // CHANGE: Return the added user
    }

    // Get user by ID
    public getUserById(id: number): User | null { // CHANGE: Return null if user not found
        return this.users.find(user => user.id === id);
    }

    // Update user
    // CHANGE: Return type to void, throw error if user not found
    public updateUser(id: number, updates: Partial<User>): void {
        const index = this.users.findIndex(user => user.id === id);
        if (index !== -1) {
            // Apply updates
            this.users[index] = { ...this.users[index], ...updates };
        }
        else {
            throw new Error(`User with ID ${id} not found`);
        }
    }

    // Delete user
    // CHANGE: Return type to void, throw error if user not found
    public deleteUser(id: number): void {
        const index = this.users.findIndex(user => user.id === id);
        if (index !== -1) {
            this.users.splice(index, 1);
        }
        else {
            throw new Error(`User with ID ${id} not found`);
        }
    }

    // Get users by role
    public getUsersByRole(role: UserRole): User[] {
        return this.users.filter(user => user.role === role); // CHANGE: changed = to ===
    }

    // Get user statistics
    public getUserStats(): UserStats {
        const roleDistribution = {
            admin: this.getUsersByRole('admin').length,
            editor: this.getUsersByRole('editor').length,
            viewer: this.getUsersByRole('viewer').length
        }
        return {
            totalUsers: this.users.length,
            activeUsers: this.users.filter(u => u.active).length,
            roleDistribution: roleDistribution,
            avgLastLogin: this.getAvgLastLogin()
        }
    }

    // Search users
    public searchUsers(query: string): User[] {
        query = query.toLowerCase();
        return this.users.filter(user => {
            return user.name.toLowerCase().includes(query) ||
                user.email.toLowerCase().includes(query);
        });
    }

    // Get next available ID
    private getNextId(): number {
        const maxId = Math.max(...this.users.map(user => user.id));
        return maxId + 1;
    }

    private getAvgLastLogin(): Date | null {
        const usersWithLastLogin: User[] = this.users.filter(u => u.lastLogin);
        if (!usersWithLastLogin.length) {
            return null;
        }
        const total = usersWithLastLogin.reduce((acc, u) => acc + u.lastLogin.getTime(), 0);
        const avg = total / usersWithLastLogin.length;
        return new Date(avg);
    }

}
