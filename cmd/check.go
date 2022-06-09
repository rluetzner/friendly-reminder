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

// checkCmd represents the check command
var checkCmd = &cobra.Command{
	Use:   "check",
	Short: "Check reminders for today",
	Long: `Check reminders for today.
This command will output the names of people for which the specified reminder period has passed. The order is sorted by the people most overdue.
Optionally this command can be used to output all contacts, even those for which the reminder period has not yet passed.

#1 Output all due or overdue contacts.
friendly-reminder check

#2 Output all contacts.
friendly-reminder check --all`,
	Run: func(cmd *cobra.Command, args []string) {
		switchAll, _ := cmd.Flags().GetBool("all")
		fmt.Printf("check called with all: %t\n", switchAll)
	},
}

func init() {
	rootCmd.AddCommand(checkCmd)
	checkCmd.Flags().BoolP("all", "a", false, "Include friends you contacted recently")
}
