/*
Copyright © 2022 Robert Lützner

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
*/
package cmd

import (
	"fmt"

	"github.com/spf13/cobra"
)

// addCmd represents the add command
var addCmd = &cobra.Command{
	Use:   "add",
	Short: "Add a new contact",
	Long: `Add a new contact you want to remember.

Examples:

#1 Reminder for 'Omar Cabbage'.
friendly-reminder add --name "Omar Cabbage"

#2 Reminder for 'Mom' every 14 days.
friendly-reminder add --name Mom --days 14`,
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("add called")
	},
}

func init() {
	rootCmd.AddCommand(addCmd)
	addCmd.Flags().String("name", "", "The name of the person you want to stay in touch with")
	addCmd.Flags().Int("days", 0, "How many days between reminders")
	addCmd.MarkFlagRequired("name")
}
